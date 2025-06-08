from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.post("/notify")
async def notify(request: Request):
    body = await request.json()
    return {
        "status": "notification sent",
        "to": body.get("email", "unknown")
    }