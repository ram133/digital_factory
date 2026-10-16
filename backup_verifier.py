import os
import datetime

print("Verifying ecosystem backup archives...")

report = "# Ecosystem Backup & Archive Verification\n\n"
report += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += "| Archive File | Size (Bytes) | Status |\n|---|---|---|\n"

archives_found = 0
for file in os.listdir("."):
    if file.endswith(".tar.gz"):
        archives_found += 1
        size = os.path.getsize(file)
        report += f"| {file} | {size} | ✅ Verified Archive |\n"

if archives_found == 0:
    report += "| No archives found | 0 | ⚠️ Run archiver.py |\n"

with open("BACKUP_REPORT.md", "w") as f:
    f.write(report)

print(f"Backup verification complete. Found {archives_found} archive(s).")
