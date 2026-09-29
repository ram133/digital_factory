from fastapi import FastAPI
import json
import os

app = FastAPI(title="Digital Factory API")

@app.get("/")
def read_root():
    return {"status": "active", "factory": "Digital Factory Core"}

@app.get("/daily-summary")
def get_daily_summary():
    if os.path.exists("daily_report.json"):
        with open("daily_report.json") as f:
            return json.load(f)
    return {"status": "No daily report found yet."}
