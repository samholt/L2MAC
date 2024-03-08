from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	email = Column(String, unique=True, nullable=False)
	username = Column(String, unique=True, nullable=False)
	password = Column(String, nullable=False)
	profile_picture = Column(String)
	bio = Column(String)
	website_link = Column(String)
	location = Column(String)
	is_private = Column(Boolean, default=False)
