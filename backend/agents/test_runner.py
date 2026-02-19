"""
Runs pytest and gathers failure information.
"""

import subprocess


class TestRunner:
    """Executes pytest and parses results."""

    def run_tests(self, repo_path):
        """Run pytest and return number of failures."""
        print("🧪 Running tests...")

        try:
            result = subprocess.run(
                ["python", "-m", "pytest"],
                cwd=repo_path,
                capture_output=True,
                text=True
            )

            output = result.stdout + result.stderr
            print(output)

            return self._parse_failures(output)

        except Exception as e:
            print("⚠️ Test execution error:", e)
            return 0

    def collect_failures(self, repo_path):
        """Collect full pytest output."""
        try:
            result = subprocess.run(
                ["python", "-m", "pytest"],
                cwd=repo_path,
                capture_output=True,
                text=True
            )
            return result.stdout + result.stderr
        except Exception:
            return ""

    def _parse_failures(self, output):
        """Extract number of failed tests."""
        for line in output.splitlines():
            if "failed" in line.lower():
                parts = line.split()
                for part in parts:
                    if part.isdigit():
                        return int(part)
        return 0
