import os
import json
import datetime

print("Running Social Factory Traffic Generator...")

inventory_path = os.path.expanduser("~/digital_factory/repo_inventory.json")
if os.path.exists(inventory_path):
    with open(inventory_path, "r") as f:
        data = json.load(f)
    
    # Handle if inventory is a dict or list
    repos = data.get("repositories", data) if isinstance(data, dict) else data
    
    if repos and isinstance(repos, list):
        # Filter out invalid entries
        valid_repos = [r for r in repos if isinstance(r, dict)]
        if valid_repos:
            latest_repo = sorted(valid_repos, key=lambda x: x.get("updatedAt", ""), reverse=True)[0]
            
            brief = f"# Automated Social Media Brief\n\n"
            brief += f"Timestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n"
            brief += f"Featured Project: {latest_repo.get("name")}\n"
            brief += f"URL: {latest_repo.get("url")}\n"
            brief += f"Suggested Short Title: Check out this autonomous web app! #{latest_repo.get("name")} #Shorts #DigitalFactory\n"
            
            with open("SOCIAL_BRIEF.md", "w") as f:
                f.write(brief)
            print(f"Social brief generated for: {latest_repo.get("name")}")
        else:
            print("No valid repo dictionaries found.")
    else:
        print("Repository inventory format unrecognized.")
else:
    print("No repo inventory found yet.")

# Generate a video script template for automated rendering
video_script = f"""# YouTube Short Video Script
## Title: Check out {latest_repo.get("name")}!
### URL: {latest_repo.get("url")}

- [0:00 - 0:02] Hook: Show iPhone opening Safari to {latest_repo.get("name")} live web app.
- [0:02 - 0:08] Feature: Scroll through the PWA interface, demonstrating autonomous automation.
- [0:08 - 0:11] Outro: Call to action - Check link in description to explore the full digital factory!
"""

with open("VIDEO_SCRIPT.md", "w") as f:
    f.write(video_script)
print("Video storyboard script generated successfully.")

import urllib.request

def publish_to_youtube():
    # Placeholder for YouTube Data API v3 integration using OAuth credentials
    print("Checking YouTube Data API integration for automated upload...")
    print("Ready for YouTube API token configuration.")

if __name__ == "__main__":
    publish_to_youtube()
