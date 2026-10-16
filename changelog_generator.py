import subprocess
import datetime

print("Generating ecosystem changelog from git history...")
git_log = subprocess.run(["git", "log", "-n", "20", "--pretty=format:%h - %an, %ar : %s"], capture_output=True, text=True).stdout

changelog = "# Ecosystem Changelog\n\n"
changelog += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
changelog += "## Recent Git Activity\n\n```text\n" + git_log + "\n```\n"

with open("CHANGELOG.md", "w") as f:
    f.write(changelog)

print("Changelog generated successfully.")
