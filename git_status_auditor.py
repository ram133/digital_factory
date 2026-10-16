import subprocess
import datetime

print("Running git status and branch telemetry...")
git_status = subprocess.run(["git", "status", "--short"], capture_output=True, text=True).stdout
git_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()

report = "# Ecosystem Git Status & Telemetry\n\n"
report += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += f"**Active Branch:** `{git_branch}`\n\n"
report += "## Working Tree Status\n\n```text\n" + (git_status if git_status else "Working tree clean.") + "\n```\n"

with open("GIT_STATUS_REPORT.md", "w") as f:
    f.write(report)

print("Git status report generated successfully.")
