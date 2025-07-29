class BaseAgent:
    """Base class for AI agents."""

    def __init__(self, config: dict):
        self.config = config

    def run(self, *args, **kwargs):
        raise NotImplementedError("Agent run method must be implemented")
