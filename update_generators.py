import json
import random
from datetime import datetime

def generate_category_asset():
    days = ["Monday: Tech/AI", "Tuesday: Guam Guide", "Wednesday: Audio/Music", "Thursday: PWA/Code", "Friday: Local Business", "Saturday: Creative", "Sunday: Recap"]
    today_idx = datetime.now().weekday()
    return {"type": "Category Scheduled", "schedule": days[today_idx], "asset": f"Scheduled content for {days[today_idx]}"}

def generate_random_asset():
    niches = ["AI Automation", "Guam Tourism", "Synthwave Audio", "SaaS Boilerplates", "Quantum Multiverse", "Floating Habitation"]
    chosen = random.choice(niches)
    return {"type": "Random Niche", "niche": chosen, "asset": f"Exploratory asset for {chosen}"}

def generate_trending_asset():
    trends = ["Qwen 3.8 Benchmarks", "Local PWA Deployment", "Binaural Frequency Synthesis"]
    chosen = random.choice(trends)
    return {"type": "Trending Dynamic", "topic": chosen, "asset": f"Real-time summary asset for {chosen}"}

def run_daily_pipeline():
    report = {
        "timestamp": datetime.now().isoformat(),
        "item_1_category": generate_category_asset(),
        "item_2_random": generate_random_asset(),
        "item_3_trending": generate_trending_asset()
    }
    with open("daily_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Generated 3 daily assets successfully.")

if __name__ == "__main__":
    run_daily_pipeline()
