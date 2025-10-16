"""RAIL Score API client implementation."""

import requests
from typing import Optional, Dict, Any, List
from .models import (
    RailScoreResponse,
    GenerateResponse,
    RegenerateResponse,
    ToneAnalyzeResponse,
    ToneMatchResponse,
    ComplianceResponse,
    DimensionDetails,
    OverallAnalysis,
    EvaluationMetadata,
    ResponseMetadata,
    GenerationMetadata,
    RailScores,
    ImprovementDetail,
    ToneProfile,
    ToneCharacteristics,
)
from .exceptions import (
    RailScoreError,
    AuthenticationError,
    RateLimitError,
    InsufficientCreditsError,
    ValidationError,
    InsufficientTierError,
    ServiceUnavailableError,
)


class RailScoreClient:
    """
    Official RAIL Score Python SDK.

    Provides methods to interact with all RAIL Score API endpoints.

    Args:
        api_key: Your RAIL Score API key
        base_url: API base URL (default: https://api.responsibleailabs.ai)
        timeout: Request timeout in seconds (default: 30)

    Example:
        >>> client = RailScoreClient(api_key='your-api-key')
        >>> result = client.calculate(
        ...     content="AI should prioritize human welfare.",
        ...     domain='general'
        ... )
        >>> print(f"Score: {result.rail_score}/10")
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.responsibleailabs.ai",
        timeout: int = 30,
    ):
        """Initialize the RAIL Score client."""
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "X-API-Key": api_key,
                "Content-Type": "application/json",
            }
        )

    def _request(
        self,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make HTTP request to API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            json: JSON request body
            params: Query parameters

        Returns:
            Parsed JSON response

        Raises:
            RailScoreError: For API errors
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=json,
                params=params,
                timeout=self.timeout,
            )

            # Handle error responses
            if not response.ok:
                self._handle_error(response)

            return response.json()

        except requests.exceptions.Timeout:
            raise RailScoreError("Request timeout")
        except requests.exceptions.RequestException as e:
            raise RailScoreError(f"Network error: {str(e)}")

    def _handle_error(self, response: requests.Response):
        """Handle API error responses."""
        try:
            error_data = response.json()
            error_message = error_data.get("error", {}).get(
                "message", "Unknown error"
            )
        except:
            error_message = response.text or "Unknown error"

        if response.status_code == 401:
            raise AuthenticationError(error_message, response.status_code, error_data)
        elif response.status_code == 429:
            raise RateLimitError(error_message, response.status_code, error_data)
        elif response.status_code == 402:
            raise InsufficientCreditsError(
                error_message, response.status_code, error_data
            )
        elif response.status_code == 400:
            raise ValidationError(error_message, response.status_code, error_data)
        elif response.status_code == 403:
            raise InsufficientTierError(
                error_message, response.status_code, error_data
            )
        elif response.status_code == 503:
            raise ServiceUnavailableError(
                error_message, response.status_code, error_data
            )
        else:
            raise RailScoreError(error_message, response.status_code, error_data)

    def calculate(
        self,
        content: str,
        domain: str = "general",
        explain_scores: bool = True,
        source: Optional[str] = None,
        model_preference: Optional[str] = None,
        custom_weights: Optional[Dict[str, float]] = None,
    ) -> RailScoreResponse:
        """
        Calculate RAIL score for content.

        Args:
            content: Text content to evaluate (20-50000 characters)
            domain: Content domain (general, healthcare, law, hr, politics, news, finance)
            explain_scores: Include detailed explanations for scores
            source: Content source (chatgpt, gemini, claude, grok, custom, pasted)
            model_preference: LLM preference (openai, gemini, both)
            custom_weights: Custom dimension weights (must sum to 1.0)

        Returns:
            RailScoreResponse with score, grade, and dimension analysis

        Raises:
            RailScoreError: If API request fails

        Example:
            >>> result = client.calculate(
            ...     content="AI should prioritize human welfare.",
            ...     domain='general'
            ... )
            >>> print(f"Score: {result.rail_score}/10 ({result.grade})")
        """
        payload = {
            "content": content,
            "domain": domain,
            "explain_scores": explain_scores,
        }

        if source:
            payload["source"] = source
        if model_preference:
            payload["model_preference"] = model_preference
        if custom_weights:
            payload["custom_weights"] = custom_weights

        response = self._request("POST", "/api/v1/railscore/ui/calculate", json=payload)
        data = response["data"]
        metadata = response.get("metadata")

        # Parse dimension scores
        dimension_scores = {}
        for dim, details in data["dimension_scores"].items():
            dimension_scores[dim] = DimensionDetails(
                score=details["score"],
                grade=details["grade"],
                explanation=details["explanation"],
                suggestions=details["suggestions"],
            )

        # Parse overall analysis
        overall_analysis = OverallAnalysis(
            strengths=data["overall_analysis"]["strengths"],
            weaknesses=data["overall_analysis"]["weaknesses"],
            top_priority=data["overall_analysis"]["top_priority"],
        )

        # Parse evaluation metadata
        eval_meta = data["evaluation_metadata"]
        evaluation_metadata = EvaluationMetadata(
            evaluation_time_ms=eval_meta["evaluation_time_ms"],
            model_used=eval_meta["model_used"],
            cached=eval_meta["cached"],
            trace_id=eval_meta["trace_id"],
            domain=eval_meta["domain"],
            source=eval_meta.get("source"),
        )

        # Parse response metadata
        response_metadata = None
        if metadata:
            response_metadata = ResponseMetadata(
                credits_used=metadata["credits_used"],
                credits_remaining=metadata["credits_remaining"],
                trace_id=metadata["trace_id"],
                tier=metadata["tier"],
            )

        return RailScoreResponse(
            rail_score=data["rail_score"],
            grade=data["grade"],
            dimension_scores=dimension_scores,
            overall_analysis=overall_analysis,
            evaluation_metadata=evaluation_metadata,
            metadata=response_metadata,
        )

    def generate(
        self,
        prompt: str,
        length: str = "medium",
        context: Optional[Dict[str, str]] = None,
        model: str = "openai",
        rail_requirements: Optional[Dict[str, Any]] = None,
    ) -> GenerateResponse:
        """
        Generate content with RAIL checks.

        Args:
            prompt: Generation prompt
            length: Content length (short, medium, long)
            context: Context for generation (purpose, industry, target_audience, tone)
            model: LLM model (openai, gemini)
            rail_requirements: RAIL requirements for content

        Returns:
            GenerateResponse with content and RAIL scores

        Example:
            >>> result = client.generate(
            ...     prompt="Write about AI ethics in healthcare",
            ...     length="medium",
            ...     context={"purpose": "blog_post", "tone": "professional"}
            ... )
            >>> print(result.content)
        """
        payload = {
            "prompt": prompt,
            "length": length,
            "model": model,
        }

        if context:
            payload["context"] = context
        if rail_requirements:
            payload["rail_requirements"] = rail_requirements

        response = self._request("POST", "/api/v1/railscore/ui/generate", json=payload)
        data = response["data"]
        metadata = response.get("metadata")

        # Parse generation metadata
        gen_meta = data["generation_metadata"]
        generation_metadata = GenerationMetadata(
            model=gen_meta["model"],
            attempts=gen_meta["attempts"],
            generation_time_ms=gen_meta["generation_time_ms"],
        )

        # Parse RAIL scores
        rail_data = data["rail_scores"]
        rail_scores = RailScores(
            rail_score=rail_data["rail_score"],
            dimension_scores=rail_data["dimension_scores"],
            requirements_met=rail_data["requirements_met"],
            failed_requirements=rail_data["failed_requirements"],
        )

        # Parse response metadata
        response_metadata = None
        if metadata:
            response_metadata = ResponseMetadata(
                credits_used=metadata["credits_used"],
                credits_remaining=metadata["credits_remaining"],
                trace_id=metadata["trace_id"],
                tier=metadata["tier"],
            )

        return GenerateResponse(
            content=data["content"],
            generation_metadata=generation_metadata,
            rail_scores=rail_scores,
            generation_history=data["generation_history"],
            metadata=response_metadata,
        )

    def regenerate(
        self,
        original_content: str,
        improve_dimensions: List[str],
        user_notes: Optional[str] = None,
        keep_structure: bool = True,
        keep_tone: bool = True,
    ) -> RegenerateResponse:
        """
        Regenerate content with improvements.

        Args:
            original_content: Original content to improve
            improve_dimensions: RAIL dimensions to improve
            user_notes: Additional improvement instructions
            keep_structure: Keep original structure
            keep_tone: Keep original tone

        Returns:
            RegenerateResponse with improved content

        Example:
            >>> result = client.regenerate(
            ...     original_content="Original text here",
            ...     improve_dimensions=["fairness", "safety"]
            ... )
            >>> print(result.content)
        """
        payload = {
            "original_content": original_content,
            "feedback": {
                "improve_dimensions": improve_dimensions,
                "keep_structure": keep_structure,
                "keep_tone": keep_tone,
            },
        }

        if user_notes:
            payload["feedback"]["user_notes"] = user_notes

        response = self._request(
            "POST", "/api/v1/railscore/ui/regenerate", json=payload
        )
        data = response["data"]
        metadata = response.get("metadata")

        # Parse improvements
        improvements = {}
        for dim, details in data["improvements"].items():
            improvements[dim] = ImprovementDetail(
                before=details["before"],
                after=details["after"],
                improvement=details["improvement"],
            )

        # Parse response metadata
        response_metadata = None
        if metadata:
            response_metadata = ResponseMetadata(
                credits_used=metadata["credits_used"],
                credits_remaining=metadata["credits_remaining"],
                trace_id=metadata["trace_id"],
                tier=metadata["tier"],
            )

        return RegenerateResponse(
            content=data["content"],
            improvements=improvements,
            changes_made=data["changes_made"],
            overall_scores=data["overall_scores"],
            metadata=response_metadata,
        )

    def analyze_tone(
        self,
        sources: List[Dict[str, str]],
        create_profile: bool = False,
        profile_name: Optional[str] = None,
    ) -> ToneAnalyzeResponse:
        """
        Analyze tone from sources.

        Args:
            sources: List of sources (type: url/text, value: content)
            create_profile: Create reusable tone profile
            profile_name: Name for the tone profile

        Returns:
            ToneAnalyzeResponse with tone profile

        Example:
            >>> result = client.analyze_tone(
            ...     sources=[{"type": "url", "value": "https://example.com"}],
            ...     create_profile=True,
            ...     profile_name="Brand Voice"
            ... )
            >>> print(result.tone_profile.characteristics.formality)
        """
        payload = {
            "sources": sources,
            "create_profile": create_profile,
        }

        if profile_name:
            payload["profile_name"] = profile_name

        response = self._request(
            "POST", "/api/v1/railscore/ui/tone/analyze", json=payload
        )
        data = response["data"]
        metadata = response.get("metadata")

        # Parse tone profile
        profile_data = data["tone_profile"]
        char_data = profile_data["characteristics"]

        characteristics = ToneCharacteristics(
            formality=char_data["formality"],
            complexity=char_data["complexity"],
            emotion=char_data["emotion"],
            technical_level=char_data["technical_level"],
            sentence_structure=char_data["sentence_structure"],
            vocabulary_level=char_data["vocabulary_level"],
            voice=char_data["voice"],
            style_markers=char_data["style_markers"],
        )

        tone_profile = ToneProfile(
            profile_id=profile_data["profile_id"],
            name=profile_data["name"],
            characteristics=characteristics,
            created_at=profile_data["created_at"],
        )

        # Parse response metadata
        response_metadata = None
        if metadata:
            response_metadata = ResponseMetadata(
                credits_used=metadata["credits_used"],
                credits_remaining=metadata["credits_remaining"],
                trace_id=metadata["trace_id"],
                tier=metadata["tier"],
            )

        return ToneAnalyzeResponse(
            tone_profile=tone_profile,
            metadata=response_metadata,
        )

    def match_tone(
        self,
        content: str,
        tone_profile_id: Optional[str] = None,
        tone_reference_urls: Optional[List[str]] = None,
        adjustment_level: str = "moderate",
    ) -> ToneMatchResponse:
        """
        Match content to tone profile.

        Args:
            content: Content to adjust
            tone_profile_id: Previously created tone profile ID
            tone_reference_urls: Reference URLs for tone
            adjustment_level: Adjustment strength (subtle, moderate, strong)

        Returns:
            ToneMatchResponse with matched content

        Example:
            >>> result = client.match_tone(
            ...     content="Content to match",
            ...     tone_profile_id="profile_123",
            ...     adjustment_level="moderate"
            ... )
            >>> print(result.matched_content)
        """
        payload = {
            "content": content,
            "adjustment_level": adjustment_level,
        }

        if tone_profile_id:
            payload["tone_profile_id"] = tone_profile_id
        if tone_reference_urls:
            payload["tone_reference_urls"] = tone_reference_urls

        response = self._request(
            "POST", "/api/v1/railscore/ui/tone/match", json=payload
        )
        data = response["data"]
        metadata = response.get("metadata")

        # Parse response metadata
        response_metadata = None
        if metadata:
            response_metadata = ResponseMetadata(
                credits_used=metadata["credits_used"],
                credits_remaining=metadata["credits_remaining"],
                trace_id=metadata["trace_id"],
                tier=metadata["tier"],
            )

        return ToneMatchResponse(
            matched_content=data["matched_content"],
            match_score=data["match_score"],
            adjustments_made=data["adjustments_made"],
            comparison=data["comparison"],
            metadata=response_metadata,
        )

    def check_compliance(
        self,
        content: str,
        framework: str,
        **kwargs,
    ) -> ComplianceResponse:
        """
        Check compliance against framework.

        Args:
            content: Content to evaluate
            framework: Compliance framework (gdpr, nist, hipaa, soc2)
            **kwargs: Framework-specific options

        Returns:
            ComplianceResponse with compliance results

        Example:
            >>> result = client.check_compliance(
            ...     content="Privacy policy text",
            ...     framework="gdpr"
            ... )
            >>> print(f"Status: {result.compliance_status}")
        """
        payload = {
            "content": content,
            **kwargs,
        }

        response = self._request(
            "POST", f"/api/v1/railscore/compliance/{framework}", json=payload
        )
        data = response["data"]
        metadata = response.get("metadata")

        # Parse response metadata
        response_metadata = None
        if metadata:
            response_metadata = ResponseMetadata(
                credits_used=metadata["credits_used"],
                credits_remaining=metadata["credits_remaining"],
                trace_id=metadata["trace_id"],
                tier=metadata["tier"],
            )

        return ComplianceResponse(
            overall_score=data["overall_score"],
            compliance_status=data["compliance_status"],
            criteria_scores=data["criteria_scores"],
            violations=data["violations"],
            recommendations=data["recommendations"],
            metadata=response_metadata,
        )

    def health(self) -> Dict[str, Any]:
        """
        Check API health status.

        Returns:
            Health status response

        Example:
            >>> health = client.health()
            >>> print(health["status"])
        """
        response = self._request("GET", "/healthz")
        return response

    def version(self) -> Dict[str, str]:
        """
        Get API version information.

        Returns:
            Version information

        Example:
            >>> version = client.version()
            >>> print(version["version"])
        """
        response = self._request("GET", "/version")
        return response
