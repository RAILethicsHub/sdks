# RAIL Score SDKs

Official client libraries for the [RAIL Score API](https://responsibleailabs.ai) - Evaluate AI-generated content across 8 dimensions of Responsible AI.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Overview

RAIL Score provides comprehensive evaluation of AI-generated content across 8 critical dimensions:

1. **Fairness** - Bias detection and equitable treatment
2. **Safety** - Toxicity and harmful content detection
3. **Reliability** - Factual accuracy and consistency
4. **Transparency** - Clear reasoning and source citation
5. **Privacy** - PII detection and data protection
6. **Accountability** - Verifiable claims and attribution
7. **Inclusivity** - Diverse perspectives and inclusive language
8. **User Impact** - Emotional tone and audience appropriateness

---

## 📦 Available SDKs

### Python SDK

[![PyPI version](https://badge.fury.io/py/rail-score-sdk.svg)](https://pypi.org/project/rail-score-sdk/1.0.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Status:** ✅ Production Ready (v1.0.0)

```bash
pip install rail-score-sdk
```

**Features:**
- ✅ Full API coverage (calculate, generate, regenerate, tone, compliance)
- ✅ Type-safe with complete type hints
- ✅ Comprehensive error handling
- ✅ 9 production-ready examples
- ✅ GitHub Actions CI/CD
- ✅ Supports Python 3.8 - 3.12

**Documentation:** [python/README.md](python/README.md)

**Quick Start:**
```python
from rail_score_sdk import RailScoreClient

client = RailScoreClient(api_key='your-api-key')
result = client.calculate(
    content="AI should prioritize human welfare and be transparent.",
    domain='general'
)
print(f"RAIL Score: {result.rail_score}/10")
```

---

### JavaScript/TypeScript SDK

**Status:** 🚧 Coming Soon

- Node.js and Browser support
- TypeScript-first with full type definitions
- Promise-based async API
- Comprehensive examples

**Planned Release:** Q1 2025

---

### Go SDK

**Status:** 📋 Planned

- Idiomatic Go implementation
- Full concurrency support
- Context-aware API
- Built-in retry logic

**Planned Release:** Q2 2025

---

### Java SDK

**Status:** 📋 Planned

- Java 11+ support
- Maven and Gradle support
- Reactive API support
- Spring Boot integration

**Planned Release:** Q2 2025

---

## 💳 Subscription Plans

All SDKs work with the same RAIL Score subscription:

| Plan | Monthly Credits | Auto-Renewal | Price (Monthly) | Price (Yearly/month) |
|------|-----------------|--------------|-----------------|---------------------|
| **Free** | 100 | Every 30 days | Free | Free |
| **Pro** | 1,000 | Every 30 days | ₹2,399 / $29 | ₹1,999 / $23 |
| **Business** | 10,000 | Every 30 days | ₹21,999 / $247 | ₹18,999 / $214 |
| **Enterprise** | 50,000 | Every 30 days | Contact Sales | Contact Sales |

**Credit Details:**
- Monthly tier credits expire in 30 days
- Purchased topup credits never expire
- Credits shared across all SDKs

**Get Started:** https://responsibleailabs.ai/dashboard

---

## 📊 Rate Limits

| Endpoint Type | Rate Limit |
|---------------|------------|
| **API Endpoints** | 60 requests / minute |
| **Auth Endpoints** | 5 requests / 15 minutes |

Rate limits apply per API key, regardless of which SDK you use.

---

## 🚀 Common Use Cases

### Content Quality Assurance
```
✓ Evaluate AI-generated content before publishing
✓ Identify and improve weak dimensions
✓ Ensure compliance with ethical guidelines
✓ Track content quality metrics over time
```

### Brand Voice Consistency
```
✓ Analyze existing content to create tone profiles
✓ Match new content to established brand voice
✓ Maintain consistency across content library
✓ Adjust tone for different audiences
```

### Compliance & Governance
```
✓ Check GDPR compliance for privacy policies
✓ Validate HIPAA compliance for healthcare content
✓ Ensure NIST cybersecurity standards
✓ Verify SOC 2 compliance requirements
```

### Content Generation Workflows
```
✓ Generate content with built-in quality checks
✓ Automatically regenerate until requirements met
✓ Set minimum scores for specific dimensions
✓ Track generation attempts and improvements
```

---

## 🔗 Resources

### Documentation
- **API Documentation**: https://responsibleailabs.ai/developer/docs
- **API Reference**: https://responsibleailabs.ai/developers/api-ref
- **Getting Started Guide**: https://responsibleailabs.ai/developer/quickstart

### Platform
- **Dashboard**: https://responsibleailabs.ai/dashboard
- **Pricing**: https://responsibleailabs.ai/pricing
- **Sign Up**: https://responsibleailabs.ai/signup

### Community & Support
- **Discord**: https://responsibleailabs.ai/discord
- **Email**: research@responsibleailabs.ai
- **GitHub Issues**: https://github.com/RAILethicsHub/sdks/issues
- **Status Page**: https://status.responsibleailabs.ai

---

## 🤝 Contributing

We welcome contributions to all SDKs! Here's how you can help:

### Report Issues
- Bug reports
- Feature requests
- Documentation improvements
- Example contributions

### Submit Pull Requests
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests (if applicable)
5. Submit a pull request

See [CONTRIBUTING.md](python/CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

All SDKs are licensed under the MIT License. See [LICENSE](LICENSE) for details.

```
MIT License

Copyright (c) 2025 RAIL Score

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🗺️ Roadmap

### Q1 2025
- ✅ Python SDK v1.0.0 (Released)
- 🚧 JavaScript/TypeScript SDK v1.0.0
- 📋 Python SDK examples library expansion
- 📋 API v2 features support

### Q2 2025
- 📋 Go SDK v1.0.0
- 📋 Java SDK v1.0.0
- 📋 Ruby SDK v1.0.0
- 📋 CLI tool for all platforms

### Future
- 📋 Rust SDK
- 📋 PHP SDK
- 📋 .NET SDK
- 📋 Mobile SDKs (iOS/Android)

---

## 🏗️ Repository Structure

```
sdks/
├── python/               # Python SDK (Production Ready)
│   ├── rail_score_sdk/   # Source code
│   ├── examples/         # 9 comprehensive examples
│   ├── tests/            # Test suite
│   ├── README.md         # Python SDK documentation
│   └── pyproject.toml    # Package configuration
│
├── javascript/           # Coming Soon
├── go/                   # Planned
├── java/                 # Planned
│
├── .github/              # GitHub Actions workflows
│   └── workflows/
│       ├── python-ci.yml
│       └── python-publish.yml
│
├── LICENSE               # MIT License
└── README.md             # This file
```

---

## 🎯 Quick Links by Language

| Language | Status | Installation | Documentation |
|----------|--------|--------------|---------------|
| **Python** | ✅ v1.0.0 | `pip install rail-score-sdk` | [Docs](python/README.md) |
| **JavaScript** | 🚧 Coming | `npm install @rail-score/sdk` | Coming Soon |
| **Go** | 📋 Planned | `go get rail-score/sdk` | Coming Soon |
| **Java** | 📋 Planned | Maven/Gradle | Coming Soon |

---

## ❓ FAQ

### Which SDK should I use?
Choose the SDK that matches your application's language. All SDKs provide the same functionality and work with the same API.

### Can I use multiple SDKs?
Yes! All SDKs share the same API key and credit pool. You can use different SDKs in different parts of your infrastructure.

### Are the SDKs open source?
Yes, all SDKs are released under the MIT License and available on GitHub.

### How do I get support?
- For SDK-specific issues: Open a GitHub issue
- For API questions: Check the documentation
- For account issues: Email research@responsibleailabs.ai
- For real-time help: Join our Discord community

### What's the difference between tiers?
The main difference is monthly credit allocation. All tiers have access to the same API features. See the pricing table above for details.

### Do credits expire?
- **Monthly tier credits**: Expire in 30 days
- **Topup credits**: Never expire
- Credits auto-renew monthly for paid plans

---

## 📊 SDK Comparison

| Feature | Python | JavaScript | Go | Java |
|---------|--------|------------|----|----|
| API Coverage | ✅ Full | 🚧 Coming | 📋 Planned | 📋 Planned |
| Type Safety | ✅ Type Hints | ✅ TypeScript | ✅ Native | ✅ Native |
| Async Support | ✅ Sync | ✅ Async/Await | ✅ Goroutines | ✅ CompletableFuture |
| Examples | ✅ 9 examples | 🚧 Coming | 📋 Planned | 📋 Planned |
| CI/CD | ✅ GitHub Actions | 🚧 Coming | 📋 Planned | 📋 Planned |
| Min Version | 3.8+ | Node 16+ | 1.18+ | 11+ |

---

## 🌐 Multi-Language Support

The RAIL Score API is language-agnostic. While we're building official SDKs for major languages, you can:

1. **Use the REST API directly** - Full documentation at https://responsibleailabs.ai/developers/api-ref
2. **Build your own client** - See our API specification
3. **Request a new SDK** - Open an issue with your language preference

---

## 📈 Stats

- **API Uptime**: 99.9%+
- **Average Response Time**: <500ms
- **Supported Languages**: 1 (Python), 3+ coming soon
- **Total Examples**: 9+ production-ready examples
- **Monthly Active Users**: Growing community

---

## 🙏 Acknowledgments

Built with ❤️ by the RAIL Score team and contributors.

Special thanks to:
- Our open-source contributors
- The Python, JavaScript, Go, and Java communities
- Early adopters and beta testers
- Everyone committed to responsible AI

---

**Ready to get started?** Choose your SDK above or [sign up for a free account](https://responsibleailabs.ai/register) today!

For questions, reach out to research@responsibleailabs.ai or join our [Discord community](https://responsibleailabs.ai/discord).
