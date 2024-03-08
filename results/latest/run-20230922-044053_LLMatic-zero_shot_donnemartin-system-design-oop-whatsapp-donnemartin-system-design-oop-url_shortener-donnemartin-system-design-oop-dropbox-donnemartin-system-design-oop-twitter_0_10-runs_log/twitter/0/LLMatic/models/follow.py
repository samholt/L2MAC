from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .user import User
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Follow(Base):
	__tablename__ = 'follows'

	follower_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
	followee_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

	follower = relationship('User', foreign_keys=[follower_id], back_populates='followees')
	followee = relationship('User', foreign_keys=[followee_id], back_populates='followers')
