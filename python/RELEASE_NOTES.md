# RAIL Score Python SDK v1.0.0

🎉 **Initial release of the official Python SDK for RAIL Score API**

The RAIL Score Python SDK provides a comprehensive, production-ready client library for evaluating AI-generated content across 8 dimensions of Responsible AI.

## 🚀 Installation

```bash
pip install rail-score-sdk
```

## ✨ Key Features

- ✅ **Comprehensive RAIL Scoring** - Evaluate content across 8 dimensions
- ✅ **Content Generation** - Generate content with automatic RAIL checks
- ✅ **Content Improvement** - Regenerate and improve existing content
- ✅ **Tone Analysis** - Extract and match tone profiles
- ✅ **Compliance Checking** - GDPR, HIPAA, NIST, SOC 2 compliance
- ✅ **Type-Safe** - Full type hints for better IDE support
- ✅ **Error Handling** - Custom exceptions for different error scenarios
- ✅ **Production Ready** - Rate limiting, retry logic, comprehensive examples

## 💳 Subscription Plans

| Plan | Monthly Credits | Price (Monthly) | Price (Yearly/month) |
|------|-----------------|-----------------|---------------------|
| **Free** | 100 | Free | Free |
| **Pro** | 1,000 | ₹2,399 / $29 | ₹1,999 / $23 |
| **Business** | 10,000 | ₹21,999 / $247 | ₹18,999 / $214 |
| **Enterprise** | 50,000 | Contact Sales | Contact Sales |

- Monthly tier credits expire in 30 days
- Purchased topup credits never expire
- Get your API key at: https://responsibleailabs.ai/dashboard

## 📊 Rate Limits

- **API Endpoints**: 60 requests / minute
- **Auth Endpoints**: 5 requests / 15 minutes

## 🎯 RAIL Dimensions

1. **Fairness** - Bias detection and equitable treatment
2. **Safety** - Toxicity and harmful content detection
3. **Reliability** - Factual accuracy and consistency
4. **Transparency** - Clear reasoning and source citation
5. **Privacy** - PII detection and data protection
6. **Accountability** - Verifiable claims and attribution
7. **Inclusivity** - Diverse perspectives and inclusive language
8. **User Impact** - Emotional tone and audience appropriateness

## 📖 Examples (9 Comprehensive Examples)

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

## 🚀 Quick Start

```python
from rail_score_sdk import RailScoreClient

# Initialize client
client = RailScoreClient(api_key='your-api-key')

# Calculate RAIL score
result = client.calculate(
    content="AI should prioritize human welfare and be transparent.",
    domain='general',
    explain_scores=True
)

print(f"RAIL Score: {result.rail_score}/10 ({result.grade})")
```

## 📦 What's Included

- **Core SDK** (`rail_score_sdk/`)
  - `client.py` - Main API client (612 lines)
  - `models.py` - Type-safe data models
  - `exceptions.py` - Custom exception hierarchy

- **Documentation**
  - `README.md` - Comprehensive guide with examples
  - `CONTRIBUTING.md` - Contribution guidelines
  - `CHANGELOG.md` - Version history
  - `DEPLOYMENT.md` - PyPI deployment guide
  - `examples/README.md` - Detailed example documentation

- **Examples** (~60KB of example code)
  - 9 production-ready examples
  - Beginner to advanced levels
  - Real-world use cases

- **Development Tools**
  - `pyproject.toml` - Modern Python packaging (PEP 517/518)
  - `MANIFEST.in` - Distribution file management
  - GitHub Actions CI/CD workflows
  - Type checking (mypy), linting (flake8), formatting (black)

## 🔗 Resources

- **PyPI Package**: https://pypi.org/project/rail-score-sdk/
- **Documentation**: https://responsibleailabs.ai/developer/docs
- **API Reference**: https://responsibleailabs.ai/developers/api-ref
- **Dashboard**: https://responsibleailabs.ai/dashboard
- **GitHub**: https://github.com/RAILethicsHub/sdks/python
- **Support**: research@responsibleailabs.ai

## 📄 License

MIT License - See [LICENSE](https://github.com/RAILethicsHub/sdks/blob/main/python/LICENSE)

---

**Full Changelog**: https://github.com/RAILethicsHub/sdks/blob/python/1.0.0/python/CHANGELOG.md
