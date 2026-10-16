import os
import tarfile
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"digital_factory_backup_{timestamp}.tar.gz"

print(f"Creating archive {backup_filename}...")

with tarfile.open(backup_filename, "w:gz") as tar:
    for root, dirs, files in os.walk("."):
        if ".git" in dirs:
            dirs.remove(".git")
        if "archive" in dirs:
            dirs.remove("archive")
        for file in files:
            if file.endswith(".tar.gz"):
                continue
            full_path = os.path.join(root, file)
            tar.add(full_path)

print(f"Backup archive successfully created: {backup_filename}")
