"""
Re-runs tests to verify fixes.
"""

from agents.test_runner import TestRunner


class VerificationAgent:
    """Verifies fixes by re-running tests."""

    def __init__(self):
        self.runner = TestRunner()

    def verify(self, repo_path):
        """Return remaining failures."""
        print("🔍 Verifying fixes...")
        return self.runner.run_tests(repo_path)
