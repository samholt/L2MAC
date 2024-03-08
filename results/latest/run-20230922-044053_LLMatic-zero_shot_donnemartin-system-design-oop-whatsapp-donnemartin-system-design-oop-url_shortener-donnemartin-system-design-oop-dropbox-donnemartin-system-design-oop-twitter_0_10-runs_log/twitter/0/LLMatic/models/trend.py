from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trend(Base):
	__tablename__ = 'trends'

	id = Column(Integer, primary_key=True)
	hashtag = Column(String, nullable=False)
	count = Column(Integer, default=0)
	timestamp = Column(DateTime(timezone=True), server_default=func.now())
