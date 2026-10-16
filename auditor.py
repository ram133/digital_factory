import os
import datetime

files_to_check = [
    "sync_all.py",
    "micro_pwa_template.html",
    "manifest.json",
    "sw.js",
    "sitemap.xml",
    "rss.xml",
    "analytics.html",
    "health_reporter.py",
    "archiver.py",
    "metrics.py"
]

report = "# Ecosystem Dependency & Component Audit\n\n"
report += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += "| Component / File | Status | Size (Bytes) |\n|---|---|---|\n"

for f in files_to_check:
    if os.path.exists(f):
        size = os.path.getsize(f)
        report += f"| {f} | ✅ Verified | {size} |\n"
    else:
        report += f"| {f} | ❌ Missing | 0 |\n"

with open("AUDIT_REPORT.md", "w") as f:
    f.write(report)

print("Dependency audit report generated successfully.")
