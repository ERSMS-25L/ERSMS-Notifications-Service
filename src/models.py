from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, func

Base = declarative_base()

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String, default="pending")
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
