import json
import os

def create_google_ads_campaign():
    if not os.path.exists("daily_report.json"):
        print("No daily_report.json found.")
        return

    with open("daily_report.json") as f:
        data = json.load(f)

    products = data.get("products", [])
    campaign_ads = []

    for p in products:
        title = p.get("title", "Digital Asset")
        price = p.get("price", "$19.00")
        file_path = p.get('file', '')
        url = f"https://ram133.github.io/digital_factory/{file_path}"

        ad_copy = {
            "campaign_name": f"Google_Search_{title.replace(' ', '_')}",
            "target_url": url,
            "headline_1": title[:30],
            "headline_2": f"Instant Access - {price}",
            "headline_3": "Secure PayPal Checkout",
            "description_1": f"Get instant access to {title}. Built for seamless workflow integration.",
            "description_2": "Deploy immediately with complete offline PWA support and source code.",
            "keywords": [
                title.lower(),
                "buy digital template",
                "pwa web app tool",
                "automation scripts"
            ]
        }
        campaign_ads.append(ad_copy)

    with open("google_ads_config.json", "w") as f:
        json.dump(campaign_ads, f, indent=2)

    print("Google Ads campaign configurations successfully generated in google_ads_config.json")

if __name__ == "__main__":
    create_google_ads_campaign()
