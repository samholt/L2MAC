from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .user import Base


class File(Base):
	__tablename__ = 'files'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	type = Column(String)
	size = Column(Float)
	path = Column(String)
	owner_id = Column(Integer, ForeignKey('users.id'))
	owner = relationship('User', back_populates='files')
	versions = relationship('FileVersion', back_populates='file')

	def __init__(self, name, type, size, path, owner):
		self.name = name
		self.type = type
		self.size = size
		self.path = path
		self.owner = owner

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_type(self):
		return self.type

	def set_type(self, type):
		self.type = type

	def get_size(self):
		return self.size

	def set_size(self, size):
		self.size = size

	def get_path(self):
		return self.path

	def set_path(self, path):
		self.path = path

	def get_owner(self):
		return self.owner

	def set_owner(self, owner):
		self.owner = owner

	def get_versions(self):
		return self.versions

	def set_versions(self, versions):
		self.versions = versions
