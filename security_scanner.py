import os
import re
import datetime

sensitive_patterns = [r"api_key", r"password", r"secret", r"token", r"private_key"]
scanned_files = 0
issues_found = 0

report = "# Ecosystem Security & Vulnerability Audit\n\n"
report += f"Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
report += "| File | Status | Findings |\n|---|---|---|\n"

for root, dirs, files in os.walk("."):
    if ".git" in dirs:
        dirs.remove(".git")
    for file in files:
        if file.endswith((".py", ".html", ".json", ".md")):
            scanned_files += 1
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read().lower()
                found = any(re.search(pat, content) for pat in sensitive_patterns)
                if found and "security_scanner" not in file:
                    issues_found += 1
                    report += f"| {file} | ⚠️ Review | Potential sensitive keyword detected |\n"
                else:
                    report += f"| {file} | ✅ Secure | No threats detected |\n"
            except Exception:
                pass

with open("SECURITY_REPORT.md", "w") as f:
    f.write(report)

print(f"Security audit complete. Scanned {scanned_files} files, flagged {issues_found} potential items.")
