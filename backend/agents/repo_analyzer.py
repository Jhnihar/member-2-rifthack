"""
Handles repository access.
"""

class RepoAnalyzer:
    """Handles repository preparation."""

    def clone_repository(self, repo_url):
        """
        Use local repository path directly.
        """
        print(f"📂 Using local repository at {repo_url}")
        return repo_url
