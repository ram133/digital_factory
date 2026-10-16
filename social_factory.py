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
