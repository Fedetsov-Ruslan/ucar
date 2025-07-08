from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FeedbackData(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, unique=True, index=True, nullable=False)
    sentiment = Column(String, nullable=False) 
    created_at = Column(String, nullable=False)