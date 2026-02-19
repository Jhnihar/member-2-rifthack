from core.orchestrator import run_agent

if __name__ == "__main__":
    print("Starting system...\n")

    result = run_agent(
        repo_url=r"C:\Users\hp\OneDrive\Documents\Desktop\failrepo",        team_name="DEVTEAM",
        leader_name="NIHAR",
        retry_limit=2
    )

    print("\nFINAL RESULT:\n")
    print(result)
