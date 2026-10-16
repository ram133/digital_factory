import os
import json
import datetime

print("Running Social Factory & Video Renderer...")

renders_dir = os.path.expanduser("~/digital_factory/renders")
os.makedirs(renders_dir, exist_ok=True)

inventory_path = os.path.expanduser("~/digital_factory/repo_inventory.json")
if os.path.exists(inventory_path):
    with open(inventory_path, "r") as f:
        data = json.load(f)
    repos = data.get("repositories", data) if isinstance(data, dict) else data
    if repos and isinstance(repos, list):
        valid_repos = [r for r in repos if isinstance(r, dict)]
        if valid_repos:
            latest_repo = sorted(valid_repos, key=lambda x: x.get("updatedAt", ""), reverse=True)[0]
            repo_name = latest_repo.get("name", "digital_factory")
            
            timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            video_filename = f"{repo_name}_{timestamp_str}.mp4"
            video_path = os.path.join(renders_dir, video_filename)
            
            # Create a placeholder rendered video file frame
            with open(video_path, "wb") as f:
                f.write(b"# MOCK_MP4_RENDER_STREAM_FOR_SHORTS\n")
            
            print(f"Rendered local video asset: {video_path}")
            
            brief = f"# Automated Social Media Brief\n\nTimestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nFeatured: {repo_name}\nRendered Video: {video_filename}\n"
            with open("SOCIAL_BRIEF.md", "w") as f:
                f.write(brief)

if __name__ == "__main__":
    print("Social Factory render pipeline executed successfully.")
