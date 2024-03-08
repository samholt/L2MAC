from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .user import User
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
	__tablename__ = 'posts'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	text = Column(String, nullable=False)
	image = Column(String)
	timestamp = Column(DateTime(timezone=True), server_default=func.now())

	user = relationship('User', back_populates='posts')
