from fastapi import FastAPI

app = FastAPI(title="AI Ops Copilot")


@app.get("/health")
async def health():
    return {"status": "healthy"}