"""
Comprehensive test script for Python SDK with live API.

This script tests all SDK methods with your running API.
By default, tests run against https://api.responsibleailabs.ai
Set RAIL_BASE_URL environment variable to test against a different API endpoint.
"""

import os
import sys
from pathlib import Path

# Add SDK to path
sys.path.insert(0, str(Path(__file__).parent))

from rail_score_sdk import (
    RailScoreClient,
    RailScoreError,
    AuthenticationError,
    ValidationError,
)


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def test_health_check(client):
    """Test health check endpoint"""
    print_section("Testing Health Check")
    try:
        health = client.health()
        print(f"✅ Health Status: {health.get('status', 'N/A')}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False


def test_version(client):
    """Test version endpoint"""
    print_section("Testing Version Endpoint")
    try:
        version = client.version()
        print(f"✅ API Version: {version.get('version', 'N/A')}")
        return True
    except Exception as e:
        print(f"❌ Version check failed: {e}")
        return False


def test_calculate(client):
    """Test calculate endpoint"""
    print_section("Testing Calculate RAIL Score")
    try:
        result = client.calculate(
            content="AI should prioritize human welfare, be transparent, and ensure fairness for all stakeholders.",
            domain='general',
            explain_scores=True
        )

        print(f"✅ Calculation successful!")
        print(f"   RAIL Score: {result.rail_score}/10")
        print(f"   Grade: {result.grade}")
        print(f"   Model Used: {result.evaluation_metadata.model_used}")
        print(f"   Evaluation Time: {result.evaluation_metadata.evaluation_time_ms}ms")
        print(f"   Cached: {result.evaluation_metadata.cached}")

        print("\n   Dimension Scores:")
        for dim, details in result.dimension_scores.items():
            print(f"      {dim}: {details.score}/10 ({details.grade})")

        print("\n   Overall Analysis:")
        print(f"      Strengths: {len(result.overall_analysis.strengths)} items")
        if result.overall_analysis.strengths:
            print(f"         - {result.overall_analysis.strengths[0]}")
        print(f"      Weaknesses: {len(result.overall_analysis.weaknesses)} items")
        if result.overall_analysis.weaknesses:
            print(f"         - {result.overall_analysis.weaknesses[0]}")
        print(f"      Top Priority: {result.overall_analysis.top_priority}")

        return True
    except Exception as e:
        print(f"❌ Calculate failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_generate(client):
    """Test generate endpoint"""
    print_section("Testing Content Generation")
    try:
        result = client.generate(
            prompt="Write a short paragraph about responsible AI in healthcare",
            length='short',
            context={
                'purpose': 'blog_post',
                'industry': 'healthcare',
                'tone': 'professional'
            },
            rail_requirements={
                'minimum_scores': {
                    'safety': 7.0,
                    'reliability': 7.0
                }
            }
        )

        print(f"✅ Generation successful!")
        print(f"   Content length: {len(result.content)} characters")
        print(f"   Content preview: {result.content[:100]}...")
        print(f"   RAIL Score: {result.rail_scores.rail_score}/10")
        print(f"   Model: {result.generation_metadata.model}")
        print(f"   Attempts: {result.generation_metadata.attempts}")
        print(f"   Generation Time: {result.generation_metadata.generation_time_ms}ms")
        print(f"   Requirements Met: {result.rail_scores.requirements_met}")

        return True
    except Exception as e:
        print(f"❌ Generate failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_error_handling(client):
    """Test error handling"""
    print_section("Testing Error Handling")

    # Test validation error
    try:
        client.calculate(content="Short")  # Too short, should fail
        print("❌ Should have raised ValidationError")
        return False
    except ValidationError as e:
        print(f"✅ Validation error caught correctly: {e.message}")
    except Exception as e:
        print(f"⚠️  Unexpected error type: {type(e).__name__}: {e}")

    return True


def test_custom_weights(client):
    """Test custom dimension weights"""
    print_section("Testing Custom Weights")
    try:
        result = client.calculate(
            content="AI systems must prioritize fairness and safety above all else.",
            domain='general',
            custom_weights={
                'fairness': 0.25,
                'safety': 0.25,
                'reliability': 0.15,
                'transparency': 0.15,
                'privacy': 0.05,
                'accountability': 0.05,
                'inclusivity': 0.05,
                'user_impact': 0.05
            }
        )

        print(f"✅ Custom weights calculation successful!")
        print(f"   RAIL Score: {result.rail_score}/10")
        print(f"   Grade: {result.grade}")

        return True
    except Exception as e:
        print(f"❌ Custom weights test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 70)
    print("  RAIL Score Python SDK - Live API Test Suite")
    print("=" * 70)

    # Get API credentials
    api_key = os.getenv('RAIL_API_KEY', 'test-api-key')
    base_url = os.getenv('RAIL_BASE_URL', 'https://api.responsibleailabs.ai')

    print(f"\nConfiguration:")
    print(f"  API Key: {api_key[:8]}...")
    print(f"  Base URL: {base_url}")

    # Create client
    print(f"\n🔧 Initializing SDK client...")
    client = RailScoreClient(
        api_key=api_key,
        base_url=base_url,
        timeout=60  # Longer timeout for generation
    )
    print(f"✅ Client created successfully")

    # Run tests
    results = {}

    results['health'] = test_health_check(client)
    results['version'] = test_version(client)
    results['calculate'] = test_calculate(client)
    results['custom_weights'] = test_custom_weights(client)
    results['generate'] = test_generate(client)
    results['error_handling'] = test_error_handling(client)

    # Summary
    print_section("Test Summary")

    total_tests = len(results)
    passed_tests = sum(1 for v in results.values() if v)
    failed_tests = total_tests - passed_tests

    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}  {test_name}")

    print(f"\n  Total: {total_tests} tests")
    print(f"  Passed: {passed_tests} tests")
    print(f"  Failed: {failed_tests} tests")

    if failed_tests == 0:
        print("\n🎉 All tests passed! SDK is working correctly.")
        return 0
    else:
        print(f"\n⚠️  {failed_tests} test(s) failed. Check the errors above.")
        return 1


if __name__ == '__main__':
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
