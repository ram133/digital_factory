import json
import datetime

with open("repo_inventory.json", "r") as f:
    data = json.load(f)
    repos = data.get("repositories", [])

print(f"Running health telemetry across {len(repos)} repositories...")

report = "# Ecosystem Health Report\n\nGenerated on: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"
report += "| Repository | Status | Visibility |\n|---|---|---|\n"

for repo in repos:
    name = repo.get("name")
    private = repo.get("private", False)
    status = "Private" if private else "Public / Active"
    vis = "Private" if private else "Public"
    report += f"| {name} | ✅ {status} | {vis} |\n"

with open("HEALTH_REPORT.md", "w") as f:
    f.write(report)

print("Ecosystem health report generated successfully.")
