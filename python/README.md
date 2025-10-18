# RAIL Score Python SDK

Official Python client library for the RAIL Score API - Evaluate AI-generated content across 8 dimensions of Responsible AI.

[![PyPI version](https://badge.fury.io/py/rail-score-sdk.svg)](https://badge.fury.io/py/rail-score-sdk)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Features

- ✅ **Comprehensive RAIL Scoring** - Evaluate content across 8 dimensions
- ✅ **Content Generation** - Generate content with automatic RAIL checks
- ✅ **Content Improvement** - Regenerate and improve existing content
- ✅ **Tone Analysis** - Extract and match tone profiles
- ✅ **Compliance Checking** - GDPR, HIPAA, NIST, SOC 2 compliance
- ✅ **Type-Safe** - Full type hints for better IDE support
- ✅ **Error Handling** - Custom exceptions for different error scenarios
- ✅ **Simple API** - Clean, intuitive interface

## 📦 Installation

```bash
pip install rail-score-sdk
```

For development:
```bash
pip install rail-score-sdk[dev]
```

## 🚀 Quick Start

```python
from rail_score_sdk import RailScoreClient

# Initialize client
client = RailScoreClient(
    api_key='your-api-key'
    # base_url is optional, defaults to https://api.responsibleailabs.ai
)

# Calculate RAIL score
result = client.calculate(
    content="AI should prioritize human welfare and be transparent.",
    domain='general',
    explain_scores=True
)

print(f"RAIL Score: {result.rail_score}/10")
print(f"Grade: {result.grade}")
print(f"Strengths: {result.overall_analysis.strengths}")
print(f"Weaknesses: {result.overall_analysis.weaknesses}")

# View dimension scores
for dim, details in result.dimension_scores.items():
    print(f"{dim}: {details.score}/10 ({details.grade})")
    print(f"  Suggestions: {details.suggestions}")
```

## 📚 Documentation

### Calculate RAIL Score

Evaluate content across all 8 RAIL dimensions:

```python
result = client.calculate(
    content="Your content here",
    domain='general',  # Options: general, healthcare, law, hr, politics, news, finance
    explain_scores=True,
    source='chatgpt',  # Optional: chatgpt, gemini, claude, grok, custom, pasted
    custom_weights={   # Optional: custom dimension weights
        'fairness': 0.15,
        'safety': 0.20,
        'reliability': 0.15,
        # ... must sum to 1.0
    }
)

print(f"Score: {result.rail_score}/10 ({result.grade})")
```

### Generate Content

Generate content with automatic RAIL quality checks:

```python
result = client.generate(
    prompt="Write about AI ethics in healthcare",
    length='medium',  # Options: short, medium, long
    context={
        'purpose': 'blog_post',
        'industry': 'healthcare',
        'target_audience': 'professionals',
        'tone': 'professional'
    },
    rail_requirements={
        'minimum_scores': {
            'safety': 8.0,
            'reliability': 7.5
        },
        'auto_regenerate': True,
        'max_attempts': 3
    }
)

print(f"Generated Content:\n{result.content}")
print(f"RAIL Score: {result.rail_scores.rail_score}")
print(f"Attempts: {result.generation_metadata.attempts}")
```

### Regenerate Content

Improve existing content based on feedback:

```python
result = client.regenerate(
    original_content="Original content here",
    improve_dimensions=['fairness', 'safety', 'inclusivity'],
    user_notes="Make it more inclusive and balanced",
    keep_structure=True,
    keep_tone=True
)

print(f"Improved Content:\n{result.content}")

# View improvements
for dim, improvement in result.improvements.items():
    print(f"{dim}: {improvement.before} → {improvement.after} (+{improvement.improvement})")
```

### Analyze Tone

Extract tone profile from URLs or text:

```python
result = client.analyze_tone(
    sources=[
        {'type': 'url', 'value': 'https://example.com/blog'},
        {'type': 'text', 'value': 'Sample text here'}
    ],
    create_profile=True,
    profile_name='Brand Voice'
)

tone = result.tone_profile.characteristics
print(f"Formality: {tone.formality}")
print(f"Complexity: {tone.complexity}")
print(f"Voice: {tone.voice}")
```

### Match Tone

Adjust content to match a specific tone:

```python
result = client.match_tone(
    content="Content to adjust",
    tone_profile_id='profile_123',  # From analyze_tone
    adjustment_level='moderate'  # Options: subtle, moderate, strong
)

print(f"Matched Content:\n{result.matched_content}")
print(f"Match Score: {result.match_score}")
```

### Check Compliance

Evaluate against compliance frameworks:

```python
# GDPR Compliance
result = client.check_compliance(
    content="Privacy policy text",
    framework='gdpr',
    context_type='privacy_policy',
    check_consent=True,
    check_data_minimization=True
)

print(f"Compliance Status: {result.compliance_status}")
print(f"Overall Score: {result.overall_score}")
print(f"Violations: {result.violations}")
print(f"Recommendations: {result.recommendations}")

# Other frameworks: 'nist', 'hipaa', 'soc2'
```

### Health Check

Check API health status:

```python
health = client.health()
print(f"Status: {health['status']}")

version = client.version()
print(f"API Version: {version['version']}")
```

## 🎯 RAIL Dimensions

The SDK evaluates content across 8 dimensions:

1. **Fairness** - Bias detection and equitable treatment
2. **Safety** - Toxicity and harmful content detection
3. **Reliability** - Factual accuracy and consistency
4. **Transparency** - Clear reasoning and source citation
5. **Privacy** - PII detection and data protection
6. **Accountability** - Verifiable claims and attribution
7. **Inclusivity** - Diverse perspectives and inclusive language
8. **User Impact** - Emotional tone and audience appropriateness

## 🔐 Authentication

The SDK supports two authentication methods:

### API Key (Recommended)
```python
client = RailScoreClient(api_key='your-rail-api-key')
```

### JWT Token
```python
from rail_score_sdk import RailScoreClients

client = RailScoreClient(api_key='your-rail-api-key')
# JWT token is automatically added to requests
```

## 🛡️ Error Handling

The SDK provides custom exceptions for different error scenarios:

```python
from rail_score_sdk import (
    RailScoreError,
    AuthenticationError,
    RateLimitError,
    InsufficientCreditsError,
    ValidationError,
)

try:
    result = client.calculate(content="...")
except AuthenticationError:
    print("Authentication failed - check your RAIL API key")
except RateLimitError:
    print("Rate limit exceeded - wait before retrying")
except InsufficientCreditsError:
    print("Out of credits - upgrade your plan")
except ValidationError as e:
    print(f"Validation error: {e.message}")
except RailScoreError as e:
    print(f"RAIL API error: {e.message}")
```

## ⚙️ Configuration

### Environment Variables

```python
import os
from rail_score_sdk import RailScoreClient

client = RailScoreClient(
    api_key=os.getenv('RAIL_API_KEY'),
    base_url=os.getenv('RAIL_BASE_URL', 'https://api.responsibleailabs.ai'),
    timeout=int(os.getenv('RAIL_TIMEOUT', '30'))
)
```

### Timeouts

```python
# Set custom timeout (in seconds)
client = RailScoreClient(
    api_key='your-api-key',
    timeout=60  # 60 seconds
)
```

## 💳 Plans & Credits

| Plan | Monthly Credits | Auto-Renewal | Price (Monthly) | Price (Yearly/month) |
|------|-----------------|--------------|-----------------|---------------------|
| **Free** | 100 | Every 30 days | Free | Free |
| **Pro** | 1,000 | Every 30 days | ₹2,399 / $29 | ₹1,999 / $23 |
| **Business** | 10,000 | Every 30 days | ₹21,999 / $247 | ₹18,999 / $214 |
| **Enterprise** | 50,000 | Every 30 days | Contact Sales | Contact Sales |

**Credit Expiry:**
- Monthly tier credits expire in 30 days
- Purchased topup credits never expire
- Get your API key at: https://responsibleailabs.ai/dashboard

## 📊 Rate Limits

| Endpoint Type | Rate Limit |
|---------------|------------|
| **API Endpoints** | 60 requests / minute |
| **Auth Endpoints** | 5 requests / 15 minutes |

**Note:** Rate limits apply per API key, regardless of plan tier.

## 🧪 Testing

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=rail_score_sdk --cov-report=html

# Format code
black rail_score_sdk/

# Type checking
mypy rail_score_sdk/
```

## 📖 Examples

See the [examples](examples/) directory for comprehensive usage examples:

**Beginner:**
- `basic_usage.py` - Basic RAIL scoring and evaluation
- `content_generation.py` - Generate content with RAIL checks
- `tone_matching.py` - Tone analysis and brand voice matching

**Intermediate:**
- `regenerate_content.py` - Improve and refine existing content
- `compliance_check.py` - GDPR, HIPAA, NIST, SOC2 compliance
- `batch_processing.py` - Process multiple texts efficiently

**Advanced:**
- `error_handling.py` - Production-ready error handling
- `advanced_features.py` - Custom weights, workflows, and analytics
- `environment_config.py` - Multi-environment deployment setup

See [examples/README.md](examples/README.md) for detailed documentation.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) first.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: https://responsibleailabs.ai/developer/docs
- **API Reference**: https://responsibleailabs.ai/developers/api-ref
- **GitHub**: https://github.com/RAILethicsHub/sdks/python/
- **PyPI**: https://pypi.org/project/rail-score-sdk/
- **Support**: research@responsibleailabs.ai

## 📞 Support

- 📧 Email:  research@responsibleailabs.ai
- 💬 Discord: [Join our community](https://responsibleailabs.ai/discord)
- 📖 Documentation: https://responsibleailabs.ai/developer/docs
- 🐛 Issues: https://github.com/RAILethicsHub/sdks/python/issues
