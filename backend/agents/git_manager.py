"""
Handles git branch creation and result preparation.
"""

import subprocess


class GitManager:
    """Manages git operations."""

    def create_branch_name(self, team_name, leader_name):
        """Create formatted branch name."""
        branch = f"{team_name}_{leader_name}_AI_Fix".upper()
        print(f"🌿 Branch prepared: {branch}")
        return branch

    def prepare_result(self, repo_path, branch_name):
        """Prepare branch with fixes."""
        print("📦 Preparing git result branch...")

        try:
            subprocess.run(["git", "checkout", "-b", branch_name],
                           cwd=repo_path, capture_output=True)

            subprocess.run(["git", "add", "."], cwd=repo_path)
            subprocess.run(["git", "commit", "-m", "AI automated fixes"],
                           cwd=repo_path, capture_output=True)
        except Exception as e:
            print("⚠️ Git operation failed:", e)
