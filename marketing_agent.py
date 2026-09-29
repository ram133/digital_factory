import json
import os
import urllib.request

def build_telegram_notification(token, chat_id, message):
    if not token or not chat_id:
        print("Telegram credentials omitted; skipping notification.")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({"chat_id": chat_id, "text": message}).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req, timeout=5)
        print("Telegram notification dispatched successfully.")
    except Exception as e:
        print(f"Telegram dispatch notice: {e}")

def run_marketing_and_notify():
    leads = []
    if os.path.exists("scraped_leads.json"):
        with open("scraped_leads.json") as f:
            leads = json.load(f)
            
    products = []
    if os.path.exists("daily_report.json"):
        with open("daily_report.json") as f:
            data = json.load(f)
            products = data.get("products", [])
            
    campaign = []
    for lead in leads:
        target_product = products[0] if products else {"title": "Automated Digital Asset", "payment_url": "crh2509@icloud.com"}
        email_draft = {
            "to": lead["email"],
            "subject": f"Automated Digital Asset: {target_product.get('title')}",
            "body": f"Hello,\n\nOur automated pipeline generated a custom digital asset: {target_product.get('title')}.\n\nAccess or purchase direct: {target_product.get('payment_url')}\n\nBest regards,\nDigital Factory Engine"
        }
        campaign.append(email_draft)
        
    with open("campaign_outreach.json", "w") as f:
        json.dump(campaign, f, indent=2)
        
    # Telegram Notification dispatch
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    summary = f"🚀 Digital Factory Daily Run Complete!\nAssets Generated: {len(products)}\nLeads Targeted: {len(leads)}\nPayPal Account: crh2509@icloud.com"
    build_telegram_notification(bot_token, chat_id, summary)

if __name__ == "__main__":
    run_marketing_and_notify()
