from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .user import User
from .post import Post
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Comment(Base):
	__tablename__ = 'comments'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	post_id = Column(Integer, ForeignKey('posts.id'))
	text = Column(String, nullable=False)
	timestamp = Column(DateTime(timezone=True), server_default=func.now())

	user = relationship('User', back_populates='comments')
	post = relationship('Post', back_populates='comments')
