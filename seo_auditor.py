import os
import datetime

print("Running SEO and meta tag audit across Digital Factory...")

report = "# Ecosystem SEO & Meta Tag Audit\n\n"
report += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += "| File | Title Tag | Viewport | Status |\n|---|---|---|---|\n"

for file in os.listdir("."):
    if file.endswith(".html"):
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        has_title = "<title>" in content
        has_viewport = "viewport" in content
        status = "✅ Optimized" if (has_title and has_viewport) else "⚠️ Needs Review"
        report += f"| {file} | {"✅" if has_title else "❌"} | {"✅" if has_viewport else "❌"} | {status} |\n"

with open("SEO_REPORT.md", "w") as f:
    f.write(report)

print("SEO audit report generated successfully.")
