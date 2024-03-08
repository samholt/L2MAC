from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	password = Column(String)
	profile_picture = Column(String)
	storage_used = Column(Float, default=0.0)
	files = relationship('File', back_populates='owner')

	def __init__(self, name, email, password, profile_picture=None):
		self.name = name
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.storage_used = 0.0

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_email(self):
		return self.email

	def set_email(self, email):
		self.email = email

	def get_password(self):
		return self.password

	def set_password(self, password):
		self.password = password

	def get_profile_picture(self):
		return self.profile_picture

	def set_profile_picture(self, profile_picture):
		self.profile_picture = profile_picture

	def get_storage_used(self):
		return self.storage_used

	def set_storage_used(self, storage_used):
		self.storage_used = storage_used
