import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app
from fastapi.testclient import TestClient

print("DEBUG:", TestClient.__module__)  # 👈 Aquí, antes de usarlo

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200

def test_ready():
    res = client.get("/ready")
    assert res.status_code == 200

def test_notify():
    res = client.post("/notify", json={"email": "carmen@example.com"})
    assert res.status_code == 200
    assert res.json()["to"] == "carmen@example.com"
    assert res.json()["status"] == "notification sent"

