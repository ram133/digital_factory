import os
import subprocess

cron_job = "0 */6 * * * cd /Users/cliffordhackett/digital_factory && python3 sync_all.py >> sync.log 2>&1\n"

current_cron = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout

if "sync_all.py" in current_cron:
    print("Cron job already exists.")
else:
    new_cron = current_cron + cron_job
    p = subprocess.run(["crontab", "-"], input=new_cron, text=True)
    if p.returncode == 0:
        print("Cron job successfully installed.")
    else:
        print("Failed to install cron job.")
