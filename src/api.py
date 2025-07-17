"""Expose the orchestrator FastAPI application as the public API."""

from src.orchestrator.orchestrator import app as app

__all__ = ["app"]

# Re-export the orchestrator API application. All route definitions are located
# in ``src.orchestrator.orchestrator`` so by importing ``app`` here we ensure
# that ``src.api.app`` refers to the exact same object.
