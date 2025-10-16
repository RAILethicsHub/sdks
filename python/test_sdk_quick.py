"""Quick test script for Python SDK"""

import sys
import os

# Add the SDK to the path
sys.path.insert(0, os.path.dirname(__file__))

from rail_score_sdk import RailScoreClient

def test_client_creation():
    """Test that client can be created"""
    print("Testing Python SDK...")

    client = RailScoreClient(
        api_key='test-key'
    )

    print(f"✅ Client created successfully")
    print(f"   API Key: {client.api_key[:8]}...")
    print(f"   Base URL: {client.base_url}")
    print(f"   Timeout: {client.timeout}s")

    return client

def test_imports():
    """Test that all components can be imported"""
    print("\nTesting imports...")

    from rail_score_sdk import (
        RailScoreClient,
        RailScoreResponse,
        GenerateResponse,
        RegenerateResponse,
        ToneAnalyzeResponse,
        ToneMatchResponse,
        ComplianceResponse,
        DimensionScores,
        RailScoreError,
        AuthenticationError,
        RateLimitError,
        InsufficientCreditsError,
        ValidationError,
    )

    print("✅ All imports successful")

    components = [
        'RailScoreClient',
        'RailScoreResponse',
        'GenerateResponse',
        'RegenerateResponse',
        'ToneAnalyzeResponse',
        'ToneMatchResponse',
        'ComplianceResponse',
        'DimensionScores',
        'RailScoreError',
        'AuthenticationError',
        'RateLimitError',
        'InsufficientCreditsError',
        'ValidationError',
    ]

    for component in components:
        print(f"   - {component}")

def test_methods_exist():
    """Test that all methods exist on the client"""
    print("\nTesting methods...")

    client = RailScoreClient(api_key='test-key')

    methods = [
        'calculate',
        'generate',
        'regenerate',
        'analyze_tone',
        'match_tone',
        'check_compliance',
        'health',
        'version',
    ]

    for method in methods:
        assert hasattr(client, method), f"Method {method} not found"
        print(f"   ✅ {method}()")

    print("✅ All methods exist")

if __name__ == '__main__':
    print("=" * 60)
    print("RAIL Score Python SDK - Quick Test")
    print("=" * 60)

    try:
        test_imports()
        test_client_creation()
        test_methods_exist()

        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nPython SDK is ready to use!")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
