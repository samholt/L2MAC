from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .user import Base, User
from .file import File


class Folder(Base):
	__tablename__ = 'folders'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	path = Column(String)
	owner_id = Column(Integer, ForeignKey('users.id'))
	owner = relationship('User')
	files = relationship('File')

	def __init__(self, name, path, owner):
		self.name = name
		self.path = path
		self.owner = owner

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_path(self):
		return self.path

	def set_path(self, path):
		self.path = path

	def get_owner(self):
		return self.owner

	def set_owner(self, owner):
		self.owner = owner

	def get_files(self):
		return self.files

	def set_files(self, files):
		self.files = files
