import json
import os

def generate_outreach_email(lead_email, asset_type, asset_title, payment_link="crh2509@icloud.com"):
    subject = f"Automated Solution: {asset_title}"
    body = f"""Hi,

I came across your site and thought you might be interested in our latest digital asset: {asset_title}.

This is an automated {asset_type} pipeline solution built to streamline operations and save processing time.

You can view details or secure access directly via PayPal ({payment_link}).

Best regards,
Digital Factory Automation
    """
    return {"to": lead_email, "subject": subject, "body": body.strip()}

def execute_marketing_campaign():
    if os.path.exists("daily_report.json"):
        with open("daily_report.json") as f:
            daily_data = json.load(f)
            
        trending_asset = daily_data.get("item_3_trending", {}).get("asset", "AI Digital Asset")
        
        # Sample outreach generation
        sample_email = "contact@example.com"
        campaign = generate_outreach_email(sample_email, "Trending AI Tool", trending_asset)
        
        with open("campaign_outreach.json", "w") as f:
            json.dump(campaign, f, indent=2)
            
        print("Marketing outreach draft successfully generated.")
    else:
        print("No daily report found. Run update_generators.py first.")

if __name__ == "__main__":
    execute_marketing_campaign()
