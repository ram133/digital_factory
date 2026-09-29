import json
import random
import os
from datetime import datetime

PRODUCTS_DIR = "products"
os.makedirs(PRODUCTS_DIR, exist_ok=True)

def build_pay_link(product_name, price="19.00"):
    base_email = "crh2509@icloud.com"
    clean_name = product_name.replace(" ", "%20")
    return f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business={base_email}&item_name={clean_name}&amount={price}&currency_code=USD"

def generate_pwa_html(title, description, price, pay_link):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
        .card {{ background: #1e293b; border-radius: 12px; padding: 32px; max-width: 480px; width: 100%; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; border: 1px solid #334155; }}
        h1 {{ color: #38bdf8; font-size: 1.5rem; margin-bottom: 12px; }}
        p {{ color: #94a3b8; line-height: 1.6; font-size: 0.95rem; margin-bottom: 24px; }}
        .price {{ font-size: 2rem; font-weight: bold; color: #f43f5e; margin-bottom: 24px; }}
        .btn {{ display: inline-block; background: #0284c7; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; transition: background 0.2s; }}
        .btn:hover {{ background: #0369a1; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{title}</h1>
        <p>{description}</p>
        <div class="price">${price}</div>
        <a href="{pay_link}" class="btn">Purchase via PayPal</a>
    </div>
</body>
</html>"""

def create_product_files():
    today = datetime.now().strftime("%Y%m%d")
    
    products = [
        {
            "filename": "pwa_core.html",
            "title": "Modular PWA Core Suite",
            "description": "Production-ready single-file Progressive Web Application boilerplate with offline caching and mobile manifest.",
            "price": "19.00"
        },
        {
            "filename": "guam_matrix.html",
            "title": "Guam Business Directory Matrix",
            "description": "Structured directory and interactive map template designed for Guam tourism and local service providers.",
            "price": "29.00"
        },
        {
            "filename": "qwen_workflow.html",
            "title": "Qwen 3.8 Local AI Orchestrator",
            "description": "Automated shell and Python execution suite for local LLM orchestration and continuous task processing.",
            "price": "15.00"
        }
    ]

    catalog = []
    for p in products:
        pay_url = build_pay_link(p["title"], p["price"])
        html_content = generate_pwa_html(p["title"], p["description"], p["price"], pay_url)
        filepath = os.path.join(PRODUCTS_DIR, p["filename"])
        
        with open(filepath, "w") as f:
            f.write(html_content)
            
        catalog.append({
            "title": p["title"],
            "description": p["description"],
            "price": f"${p['price']}",
            "payment_url": pay_url,
            "file": f"products/{p['filename']}"
        })
    
    # Generate standalone index.html for live GitHub Pages hosting
    index_html = f"""<!DOCTYPE html>
<html>
<head><title>Digital Factory Live Catalog</title><meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body style="font-family:sans-serif; background:#0f172a; color:#fff; padding:20px;">
    <h2>Digital Factory Daily Products</h2>
    <ul>
        {"".join([f'<li><a style="color:#38bdf8" href="products/{p["filename"]}">{p["title"]}</a> - ${p["price"]}</li>' for p in products])}
    </ul>
</body>
</html>"""
    with open("index.html", "w") as f:
        f.write(index_html)

    with open(f"{PRODUCTS_DIR}/daily_catalog_{today}.json", "w") as f:
        json.dump(catalog, f, indent=2)

    return catalog

def update_daily_report():
    catalog = create_product_files()
    report = {
        "timestamp": datetime.now().isoformat(),
        "status": "ready_for_sale",
        "merchant_paypal": "crh2509@icloud.com",
        "products": catalog
    }
    with open("daily_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Agentic product assembly complete. Live HTML PWAs and index generated.")

if __name__ == "__main__":
    update_daily_report()
