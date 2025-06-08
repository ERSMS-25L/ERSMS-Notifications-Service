# Notification Service (Dummy)

## Endpoints

- `GET /health` → Health check
- `GET /ready` → Readiness check
- `POST /notify` → Simulates sending a notification

## How to Run

```bash
uvicorn src.main:app --reload --port 8004
```

Or with Docker:

```bash
docker build -t notification-service .
docker run -p 8004:8004 notification-service
```