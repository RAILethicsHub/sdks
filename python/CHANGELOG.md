# Changelog

All notable changes to the RAIL Score Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-XX

### Added
- Initial release of RAIL Score Python SDK
- `RailScoreClient` class for API interactions
- Support for all RAIL Score API endpoints:
  - `calculate()` - Calculate RAIL scores for content
  - `generate()` - Generate content with RAIL checks
  - `regenerate()` - Improve existing content
  - `analyze_tone()` - Extract tone profiles from content
  - `match_tone()` - Adjust content to match tone profiles
  - `check_compliance()` - Check compliance (GDPR, HIPAA, NIST, SOC2)
  - `health()` - Check API health status
  - `version()` - Get API version information
- Comprehensive data models using dataclasses:
  - `RailScoreResponse`
  - `GenerateResponse`
  - `RegenerateResponse`
  - `ToneAnalyzeResponse`
  - `ToneMatchResponse`
  - `ComplianceResponse`
  - `DimensionScores`
- Custom exception hierarchy:
  - `RailScoreError` (base exception)
  - `AuthenticationError` (401)
  - `RateLimitError` (429)
  - `InsufficientCreditsError` (402)
  - `ValidationError` (400)
  - `InsufficientTierError` (403)
  - `ServiceUnavailableError` (503)
- Full type hints throughout the codebase
- Comprehensive documentation in README.md
- Example files:
  - `basic_usage.py` - Basic RAIL scoring
  - `content_generation.py` - Content generation
  - `tone_matching.py` - Tone analysis and matching
  - `compliance_check.py` - Compliance checking
  - `batch_processing.py` - Batch processing examples
- Development tooling:
  - Black for code formatting
  - Flake8 for linting
  - MyPy for type checking
  - Pytest for testing
- MIT License
- Python 3.8+ support

### Dependencies
- `requests>=2.28.0` - HTTP client library

### Development Dependencies
- `pytest>=7.0.0` - Testing framework
- `pytest-cov>=4.0.0` - Coverage reporting
- `black>=22.0.0` - Code formatter
- `flake8>=5.0.0` - Linter
- `mypy>=0.990` - Type checker
- `types-requests>=2.28.0` - Type stubs for requests

### Documentation
- Comprehensive README with examples
- Docstrings for all public APIs
- Contributing guidelines
- Code of conduct

### Infrastructure
- GitHub repository setup
- CI/CD pipeline with GitHub Actions
- Automated testing on multiple Python versions
- PyPI package configuration

## [Unreleased]

### Planned Features
- Async/await support for concurrent API calls
- Retry mechanism with exponential backoff
- Response caching
- Webhook support
- Batch operations API
- Streaming responses for long-running operations
- CLI tool for command-line usage
- Additional examples and tutorials

---

## Version History

### Version Numbering

We use Semantic Versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Incompatible API changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

### Types of Changes

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

---

[1.0.0]: https://github.com/RAILethicsHub/sdks/python/releases/tag/v1.0.0
