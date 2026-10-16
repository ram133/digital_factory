import os
import subprocess
import datetime

print("Initializing Local API Bridge telemetry check...")

# Gather git status and recent logs
git_status = subprocess.run(["git", "status", "--short"], capture_output=True, text=True).stdout
git_log = subprocess.run(["git", "log", "-n", "5", "--pretty=format:%h - %s"], capture_output=True, text=True).stdout

report = f"# Autonomous Agent Bridge Telemetry\n\n"
report += f"Timestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += f"## Working Tree\n```text\n{git_status or "Clean"}\n```\n\n"
report += f"## Recent Commits\n```text\n{git_log}\n```\n"

with open("BRIDGE_STATUS.md", "w") as f:
    f.write(report)

print("Agent bridge telemetry synced successfully.")
