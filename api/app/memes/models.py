from sqlalchemy import Column, String, TIMESTAMP, Integer
from sqlalchemy.sql import func

from app.database import Base

class Memes(Base):
    __tablename__ = "memes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, index=True)
    image_url = Column(String, nullable=False)
    description = Column(String)
    category = Column(String, index=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
     
    def __str__(self):
        return f"Мем {self.title}"