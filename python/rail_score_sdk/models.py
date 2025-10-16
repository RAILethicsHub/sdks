"""Data models for RAIL Score SDK."""

from dataclasses import dataclass
from typing import Dict, Any, List, Optional


@dataclass
class DimensionScores:
    """RAIL dimension scores (0-10 scale)."""

    fairness: float
    safety: float
    reliability: float
    transparency: float
    privacy: float
    accountability: float
    inclusivity: float
    user_impact: float


@dataclass
class DimensionDetails:
    """Detailed information for a single dimension."""

    score: float
    grade: str
    explanation: str
    suggestions: List[str]


@dataclass
class OverallAnalysis:
    """Overall analysis of content."""

    strengths: List[str]
    weaknesses: List[str]
    top_priority: str


@dataclass
class EvaluationMetadata:
    """Metadata about the evaluation."""

    evaluation_time_ms: int
    model_used: str
    cached: bool
    trace_id: str
    domain: str
    source: Optional[str] = None


@dataclass
class ResponseMetadata:
    """Metadata about the API response."""

    credits_used: int
    credits_remaining: int
    trace_id: str
    tier: str


@dataclass
class RailScoreResponse:
    """Response from the calculate endpoint."""

    rail_score: float
    grade: str
    dimension_scores: Dict[str, DimensionDetails]
    overall_analysis: OverallAnalysis
    evaluation_metadata: EvaluationMetadata
    metadata: Optional[ResponseMetadata] = None


@dataclass
class GenerationMetadata:
    """Metadata about content generation."""

    model: str
    attempts: int
    generation_time_ms: int


@dataclass
class RailScores:
    """RAIL scores for generated content."""

    rail_score: float
    dimension_scores: Dict[str, float]
    requirements_met: bool
    failed_requirements: List[Dict[str, Any]]


@dataclass
class GenerateResponse:
    """Response from the generate endpoint."""

    content: str
    generation_metadata: GenerationMetadata
    rail_scores: RailScores
    generation_history: List[Dict[str, Any]]
    metadata: Optional[ResponseMetadata] = None


@dataclass
class ImprovementDetail:
    """Details about dimension improvement."""

    before: float
    after: float
    improvement: float


@dataclass
class RegenerateResponse:
    """Response from the regenerate endpoint."""

    content: str
    improvements: Dict[str, ImprovementDetail]
    changes_made: List[str]
    overall_scores: Dict[str, float]
    metadata: Optional[ResponseMetadata] = None


@dataclass
class ToneCharacteristics:
    """Tone profile characteristics."""

    formality: float
    complexity: float
    emotion: float
    technical_level: float
    sentence_structure: str
    vocabulary_level: str
    voice: str
    style_markers: List[str]


@dataclass
class ToneProfile:
    """Tone profile for content."""

    profile_id: str
    name: str
    characteristics: ToneCharacteristics
    created_at: str


@dataclass
class ToneAnalyzeResponse:
    """Response from tone analyze endpoint."""

    tone_profile: ToneProfile
    metadata: Optional[ResponseMetadata] = None


@dataclass
class ToneMatchResponse:
    """Response from tone match endpoint."""

    matched_content: str
    match_score: float
    adjustments_made: List[str]
    comparison: Dict[str, Any]
    metadata: Optional[ResponseMetadata] = None


@dataclass
class ComplianceResponse:
    """Response from compliance endpoints."""

    overall_score: float
    compliance_status: str
    criteria_scores: Dict[str, float]
    violations: List[Dict[str, Any]]
    recommendations: List[str]
    metadata: Optional[ResponseMetadata] = None
