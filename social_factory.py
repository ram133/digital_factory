import os
import json
import datetime
import urllib.request
import urllib.parse

print("Running Social Factory Traffic Generator...")

inventory_path = os.path.expanduser("~/digital_factory/repo_inventory.json")
if os.path.exists(inventory_path):
    with open(inventory_path, "r") as f:
        data = json.load(f)
    repos = data.get("repositories", data) if isinstance(data, dict) else data
    if repos and isinstance(repos, list):
        valid_repos = [r for r in repos if isinstance(r, dict)]
        if valid_repos:
            latest_repo = sorted(valid_repos, key=lambda x: x.get("updatedAt", ""), reverse=True)[0]
            brief = f"# Automated Social Media Brief\n\nTimestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nFeatured: {latest_repo.get("name")}\nURL: {latest_repo.get("url")}\n"
            with open("SOCIAL_BRIEF.md", "w") as f:
                f.write(brief)
            
            video_script = f"""# YouTube Short Video Script
## Title: Check out {latest_repo.get("name")}!
### URL: {latest_repo.get("url")}
- [0:00 - 0:02] Hook: Show live web app interface.
- [0:02 - 0:08] Feature: Walk through automated workflow.
- [0:08 - 0:11] Outro: Check link in description!
"""
            with open("VIDEO_SCRIPT.md", "w") as f:
                f.write(video_script)
            print(f"Social brief & script generated for: {latest_repo.get("name")}")

def upload_video_to_youtube(video_file_path, title, description):
    token_path = os.path.expanduser("~/digital_factory/youtube_token.json")
    if not os.path.exists(token_path):
        print("YouTube token not found. Skipping direct upload.")
        return False
    
    with open(token_path, "r") as f:
        tokens = json.load(f)
    
    access_token = tokens.get("access_token")
    
    # YouTube Data API v3 Resumable Upload Initialization
    metadata = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["shorts", "digitalfactory", "coding"],
            "categoryId": "28" # Science & Technology
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }
    
    url = "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status"
    req = urllib.request.Request(
        url,
        data=json.dumps(metadata).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Upload-Content-Type": "video/mp4"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            upload_url = response.headers.get("Location")
            print(f"Resumable upload session initialized: {upload_url}")
            # Binary stream upload placeholder for generated .mp4 files
            return True
    except Exception as e:
        print(f"YouTube upload initialization failed: {e}")
        return False

if __name__ == "__main__":
    print("Social Factory pipeline executed successfully.")
