from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .user import User
from .post import Post
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Like(Base):
	__tablename__ = 'likes'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	post_id = Column(Integer, ForeignKey('posts.id'))

	user = relationship('User', back_populates='likes')
	post = relationship('Post', back_populates='likes')
