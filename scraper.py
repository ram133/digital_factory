import re
import json
import urllib.request
from bs4 import BeautifulSoup

def scrape_leads(target_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(target_url, headers=headers)
    
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Regex pattern for extracting email addresses
        emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)))
        # Filter out common false positives
        clean_emails = [e for e in emails if not e.endswith(('.png', '.jpg', '.jpeg', '.svg', '.gif'))]
        
        title = soup.title.string if soup.title else target_url
        return {"url": target_url, "title": title.strip(), "emails": clean_emails}
    except Exception as e:
        return {"url": target_url, "error": str(e), "emails": []}

if __name__ == "__main__":
    test_url = "https://example.com"
    leads = scrape_leads(test_url)
    print("Scraper completed:", json.dumps(leads, indent=2))
