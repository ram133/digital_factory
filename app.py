import streamlit as st
import requests

st.set_page_config(page_title="Digital Factory Control", layout="wide")
st.title("Digital Factory Dashboard")

st.markdown("### System Status")
st.success("Virtual Environment & Dependencies Loaded")

if st.button("Trigger Asset Generation"):
    st.info("Initiating local automated asset build pipeline...")
