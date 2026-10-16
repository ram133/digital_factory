import os

log_path = os.path.expanduser("~/digital_factory/sync.log")
err_path = os.path.expanduser("~/digital_factory/sync_error.log")

print("=== Ecosystem Sync Log ===")
if os.path.exists(log_path):
    with open(log_path, "r") as f:
        lines = f.readlines()
        print("".join(lines[-15:]))
else:
    print("No sync.log found yet.")

print("=== Ecosystem Error Log ===")
if os.path.exists(err_path):
    with open(err_path, "r") as f:
        lines = f.readlines()
        if lines:
            print("".join(lines[-10:]))
        else:
            print("No errors recorded. Clean.")
else:
    print("No sync_error.log found.")
