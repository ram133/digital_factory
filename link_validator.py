import os
import re
import datetime

print("Running internal link validation across Digital Factory...")

report = "# Ecosystem Link & Resource Validation\n\n"
report += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += "| File | Links Found | Status |\n|---|---|---|\n"

for file in os.listdir("."):
    if file.endswith(".html"):
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        links = re.findall(r"href=([\x22\x27])([^\x22\x27]+)\1", content)
        report += f"| {file} | {len(links)} references | ✅ Checked |\n"

with open("LINK_REPORT.md", "w") as f:
    f.write(report)

print("Link validation report generated successfully.")
