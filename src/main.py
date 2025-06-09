from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_session, engine
from src import models, schemas

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/ready")
async def ready():
    return {"status": "ready"}

@app.post("/notify", response_model=schemas.NotificationResponse)
async def notify(notification: schemas.NotificationCreate, session: AsyncSession = Depends(get_session)):
    new_notification = models.Notification(
        user_email=notification.user_email,
        message=notification.message,
        status="sent"  # cambiar a "queued" si metes mail service o Kafka después
    )
    session.add(new_notification)
    await session.commit()
    await session.refresh(new_notification)
    return new_notification

@app.get("/notifications/by-user/{email}", response_model=list[schemas.NotificationResponse])
async def get_notifications_by_user(email: str, session: AsyncSession = Depends(get_session)):
    stmt = select(models.Notification).where(models.Notification.user_email == email)
    result = await session.execute(stmt)
    notifications = result.scalars().all()
    return notifications
