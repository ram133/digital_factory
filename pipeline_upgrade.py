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

def create_product_files():
    today = datetime.now().strftime("%Y%m%d")
    
    # 1. Scheduled Asset
    sched_title = f"pwa_template_{today}"
    sched_content = {
        "title": "Modular PWA Core",
        "description": "Single-file Progressive Web App boilerplate with offline service worker.",
        "price": "$19.00",
        "payment_url": build_pay_link("Modular PWA Core", "19.00")
    }
    
    # 2. Niche Asset
    niche_title = f"guam_guide_{today}"
    niche_content = {
        "title": "Guam Business Directory & Map Matrix",
        "description": "Structured JSON/HTML matrix for local tourism and service integration.",
        "price": "$29.00",
        "payment_url": build_pay_link("Guam Business Directory", "29.00")
    }
    
    # 3. Trending Asset
    trend_title = f"ai_prompt_pack_{today}"
    trend_content = {
        "title": "Qwen 3.8 Local Execution & Automation Workflow",
        "description": "Automated shell and Python script package for local LLM orchestration.",
        "price": "$15.00",
        "payment_url": build_pay_link("Qwen Automation Workflow", "15.00")
    }

    catalog = [sched_content, niche_content, trend_content]
    
    # Write product files
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
    print("Upgraded pipeline generated products and PayPal buy links.")

if __name__ == "__main__":
    update_daily_report()
