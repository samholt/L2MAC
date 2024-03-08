from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .user import User
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Notification(Base):
	__tablename__ = 'notifications'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	type = Column(String, nullable=False)
	related_id = Column(Integer, nullable=False)

	user = relationship('User', back_populates='notifications')
