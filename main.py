from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Digital Factory API")

@app.get("/")
def read_root():
    return {"status": "active", "factory": "Digital Factory Core"}

@app.get("/generate")
def generate_asset():
    # Placeholder for automated media/content generation logic
    return {"result": "success", "asset_id": "item_001"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
