from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .user import User
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
	__tablename__ = 'messages'

	id = Column(Integer, primary_key=True)
	sender_id = Column(Integer, ForeignKey('users.id'))
	receiver_id = Column(Integer, ForeignKey('users.id'))
	text = Column(String, nullable=False)
	timestamp = Column(DateTime(timezone=True), server_default=func.now())

	sender = relationship('User', foreign_keys=[sender_id])
	receiver = relationship('User', foreign_keys=[receiver_id])
