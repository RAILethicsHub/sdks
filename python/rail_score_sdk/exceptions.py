"""Custom exceptions for the RAIL Score SDK."""


class RailScoreError(Exception):
    """Base exception for all RAIL Score SDK errors."""

    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response


class AuthenticationError(RailScoreError):
    """Raised when authentication fails (401)."""

    pass


class RateLimitError(RailScoreError):
    """Raised when rate limit is exceeded (429)."""

    pass


class InsufficientCreditsError(RailScoreError):
    """Raised when account has insufficient credits (402)."""

    pass


class ValidationError(RailScoreError):
    """Raised when request validation fails (400)."""

    pass


class InsufficientTierError(RailScoreError):
    """Raised when feature requires higher tier (403)."""

    pass


class ServiceUnavailableError(RailScoreError):
    """Raised when service is temporarily unavailable (503)."""

    pass
