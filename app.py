import streamlit as st
import json
import os

st.set_page_config(page_title="Digital Factory Control", layout="wide")
st.title("Digital Factory Dashboard")

st.markdown("### Daily Product Catalog & Monetization Hub")

if os.path.exists("daily_report.json"):
    with open("daily_report.json") as f:
        data = json.load(f)
    
    st.caption(f"Last Execution: {data.get('timestamp')}")
    st.success(f"Status: {data.get('status', 'Active').upper()} | Merchant: {data.get('merchant_paypal')}")
    
    cols = st.columns(3)
    products = data.get("products", [])
    
    for idx, prod in enumerate(products):
        with cols[idx % 3]:
            st.subheader(prod.get("title"))
            st.write(prod.get("description"))
            st.metric("Price", prod.get("price"))
            st.link_button("Purchase via PayPal", prod.get("payment_url"))
else:
    st.info("No daily product catalog found. Pipeline will execute at 07:00 ChST.")
