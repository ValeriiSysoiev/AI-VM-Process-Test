from src.api import app as api_app
from src.orchestrator.orchestrator import app as orch_app


def test_api_and_orchestrator_apps_are_identical():
    assert api_app is orch_app
