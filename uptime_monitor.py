import datetime
import urllib.request

endpoints = [
    "https://ram133.github.io/digital_factory/",
    "https://ram133.github.io/digital_factory/micro_pwa_template.html",
    "https://ram133.github.io/digital_factory/sitemap.xml",
    "https://ram133.github.io/digital_factory/rss.xml",
    "https://ram133.github.io/digital_factory/analytics.html",
    "https://ram133.github.io/digital_factory/api/repositories.json"
]

print("Running endpoint heartbeat check...")

log_entry = f"Heartbeat Check: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n"

for url in endpoints:
    try:
        status = urllib.request.urlopen(url, timeout=5).getcode()
        log_entry += f"  [OK] {url} -> HTTP {status}\n"
    except Exception as e:
        log_entry += f"  [FAIL] {url} -> Error: {e}\n"

with open("uptime.log", "a") as f:
    f.write(log_entry + "\n")

print("Heartbeat check complete. Log updated.")
