import os
import json

print("Running asset optimization across Digital Factory...")

for file in os.listdir("."):
    if file.endswith(".html") or file.endswith(".json"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        # Basic whitespace reduction
        optimized = "\n".join([line.strip() for line in content.splitlines() if line.strip()])
        with open(file, "w", encoding="utf-8") as f:
            f.write(optimized)
        print(f"Optimized: {file}")

print("Asset optimization complete.")
