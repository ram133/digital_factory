import json
import random
import os
from datetime import datetime

PRODUCTS_DIR = "products"
os.makedirs(PRODUCTS_DIR, exist_ok=True)

CATEGORIES = ["PWA Tool", "Guam Resource", "AI Workflow"]
NICHE_TOPICS = ["Local Service Directory", "Audio Binaural Generator", "Task Automation Engine", "Quantum Mind Map", "SaaS Payment Interface"]

def build_pay_link(product_name, price):
    base_email = "crh2509@icloud.com"
    clean_name = product_name.replace(" ", "%20")
    return f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business={base_email}&item_name={clean_name}&amount={price}&currency_code=USD"

def generate_dynamic_products():
    today = datetime.now().strftime("%Y%m%d")
    selected_topics = random.sample(NICHE_TOPICS, 3)
    
    catalog = []
    for idx, topic in enumerate(selected_topics):
        category = CATEGORIES[idx % len(CATEGORIES)]
        title = f"{category}: {topic}"
        price = str(random.choice([15, 19, 29, 39])) + ".00"
        filename = f"asset_{idx+1}_{today}.html"
        pay_url = build_pay_link(title, price)
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: system-ui, sans-serif; background: #0f172a; color: #f8fafc; padding: 2rem; display: flex; justify-content: center; }}
        .card {{ background: #1e293b; padding: 2rem; border-radius: 12px; max-width: 500px; border: 1px solid #334155; text-align: center; }}
        .btn {{ display: inline-block; margin-top: 1rem; background: #0284c7; color: white; padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{title}</h1>
        <p>Autonomously generated daily digital asset produced by Digital Factory.</p>
        <h2>${price}</h2>
        <a class="btn" href="{pay_url}">Buy via PayPal</a>
    </div>
</body>
</html>"""
        
        with open(f"{PRODUCTS_DIR}/{filename}", "w") as f:
            f.write(html_content)
            
        catalog.append({
            "title": title,
            "price": f"${price}",
            "payment_url": pay_url,
            "file": f"products/{filename}"
        })
        
    index_html = f"""<!DOCTYPE html>
<html>
<head><title>Digital Factory Live Catalog</title><meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body style="font-family:sans-serif; background:#0f172a; color:#fff; padding:20px;">
    <h2>Digital Factory Autonomous Catalog ({today})</h2>
    <ul>
        {"".join([f'<li><a style="color:#38bdf8" href="{p["file"]}">{p["title"]}</a> - {p["price"]}</li>' for p in catalog])}
    </ul>
</body>
</html>"""
    with open("index.html", "w") as f:
        f.write(index_html)
        
    with open("daily_report.json", "w") as f:
        json.dump({"timestamp": datetime.now().isoformat(), "merchant": "crh2509@icloud.com", "products": catalog}, f, indent=2)
        
    print("Autonomous product innovation cycle complete.")

if __name__ == "__main__":
    generate_dynamic_products()
