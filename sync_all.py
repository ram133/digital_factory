import subprocess, json, datetime

def run_sync():
    print("Starting Digital Factory Master Sync...")
    result = subprocess.run(["gh", "repo", "list", "ram133", "--limit", "100", "--json", "name,url,updatedAt,isPrivate"], capture_output=True, text=True)
    if result.returncode == 0:
        repos = json.loads(result.stdout)
        total = len(repos)
        inventory = {
            "sync_time": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "total_repos": total,
            "repositories": repos
        }
        with open("repo_inventory.json", "w") as f:
            json.dump(inventory, f, indent=2)
        
        html = f"""<!DOCTYPE html>
<html>
<head><title>Digital Factory Dashboard</title></head>
<body>
<h1>Digital Factory Automated Dashboard</h1>
<p>Status: Healthy | Total Repos: {total}</p>
<ul>
  <li><a href="catalog.json">Catalog JSON</a></li>
  <li><a href="health_report.json">Health Report JSON</a></li>
  <li><a href="sitemap.xml">Sitemap XML</a></li>
  <li><a href="repo_inventory.json">Repository Inventory JSON ({total} Repos)</a></li>
</ul>
</body>
</html>"""
        with open("index.html", "w") as f:
            f.write(html)
        print("Master sync completed successfully.")
    else:
        print("Sync failed:", result.stderr)

if __name__ == "__main__":
    run_sync()

