"""
Main orchestration engine for multi-agent debugging workflow.
"""

import os
from core.retry_controller import RetryController
from agents.repo_analyzer import RepoAnalyzer
from agents.test_runner import TestRunner
from agents.bug_classifier import BugClassifier
from agents.fix_generator import FixGenerator
from agents.verification import VerificationAgent
from agents.git_manager import GitManager


def run_agent(repo_url, team_name, leader_name, retry_limit=5):
    """
    Runs the multi-agent debugging workflow.

    Args:
        repo_url (str): Git repository URL
        team_name (str): Team name
        leader_name (str): Team leader name
        retry_limit (int): Maximum retry iterations

    Returns:
        dict: execution report
    """

    print("\n🚀 Starting AI Debug Orchestrator\n")

    analyzer = RepoAnalyzer()
    tester = TestRunner()
    classifier = BugClassifier()
    fixer = FixGenerator()
    verifier = VerificationAgent()
    git_manager = GitManager()

    controller = RetryController(retry_limit)

    timeline = []
    fixes_applied = 0

    repo_path = analyzer.clone_repository(repo_url)
    branch_name = git_manager.create_branch_name(team_name, leader_name)

    # initial test run
    failures = tester.run_tests(repo_path)

    if failures == 0:
        print("✅ No failures detected. Nothing to fix.")
        return {
            "status": "completed",
            "iterations": 0,
            "total_failures": 0,
            "fixes_applied": 0,
            "branch": branch_name,
            "ci_status": "passed",
            "timeline": ["No failures"]
        }

    while controller.should_retry() and failures > 0:
        print(f"\n🔁 Iteration {controller.iteration}")

        failure_data = tester.collect_failures(repo_path)
        bug_types = classifier.classify(failure_data)

        fixes = fixer.generate_fixes(repo_path, bug_types)
        fixes_applied += fixes

        failures = verifier.verify(repo_path)

        timeline.append({
            "iteration": controller.iteration,
            "failures": failures,
            "fixes": fixes
        })

        controller.next()

    ci_status = "passed" if failures == 0 else "failed"

    git_manager.prepare_result(repo_path, branch_name)

    print("\n🏁 Orchestration Completed\n")

    return {
        "status": "completed",
        "iterations": controller.iteration,
        "total_failures": failures,
        "fixes_applied": fixes_applied,
        "branch": branch_name,
        "ci_status": ci_status,
        "timeline": timeline
    }
