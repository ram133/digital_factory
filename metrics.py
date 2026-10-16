import os
import shutil
import datetime

disk_total, disk_used, disk_free = shutil.disk_usage(".")

report = "# System Metrics & Telemetry\n\n"
report += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += "| Resource | Usage / Status |\n|---|---|\n"
report += f"| Disk Total | {disk_total // (2**30)} GB |\n"
report += f"| Disk Used | {disk_used // (2**30)} GB |\n"
report += f"| Disk Free | {disk_free // (2**30)} GB |\n"
report += "| Environment | macOS Apple Silicon M3 |\n"

with open("SYSTEM_METRICS.md", "w") as f:
    f.write(report)

print("System metrics report generated successfully.")
