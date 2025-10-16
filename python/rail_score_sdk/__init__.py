"""
RAIL Score Python SDK

Official Python client library for the RAIL Score API.
Evaluate AI-generated content across 8 dimensions of Responsible AI.

Example:
    >>> from rail_score_sdk import RailScoreClient
    >>> client = RailScoreClient(api_key='your-api-key')
    >>> result = client.calculate(
    ...     content="AI should be fair and transparent.",
    ...     domain='general'
    ... )
    >>> print(f"Score: {result.rail_score} ({result.grade})")
"""

from .client import RailScoreClient
from .models import (
    RailScoreResponse,
    GenerateResponse,
    RegenerateResponse,
    ToneAnalyzeResponse,
    ToneMatchResponse,
    ComplianceResponse,
    DimensionScores,
)
from .exceptions import (
    RailScoreError,
    AuthenticationError,
    RateLimitError,
    InsufficientCreditsError,
    ValidationError,
)

__version__ = "1.0.0"
__all__ = [
    "RailScoreClient",
    "RailScoreResponse",
    "GenerateResponse",
    "RegenerateResponse",
    "ToneAnalyzeResponse",
    "ToneMatchResponse",
    "ComplianceResponse",
    "DimensionScores",
    "RailScoreError",
    "AuthenticationError",
    "RateLimitError",
    "InsufficientCreditsError",
    "ValidationError",
]
