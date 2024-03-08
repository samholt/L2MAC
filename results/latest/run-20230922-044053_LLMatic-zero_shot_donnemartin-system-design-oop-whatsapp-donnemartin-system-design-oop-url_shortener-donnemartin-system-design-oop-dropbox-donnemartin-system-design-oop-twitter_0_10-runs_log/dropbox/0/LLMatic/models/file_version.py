from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .file import Base
from datetime import datetime


class FileVersion(Base):
	__tablename__ = 'file_versions'

	id = Column(Integer, primary_key=True)
	file_id = Column(Integer, ForeignKey('files.id'))
	file = relationship('File', back_populates='versions')
	version_number = Column(Integer)
	timestamp = Column(DateTime, default=datetime.utcnow)

	def __init__(self, file, version_number):
		self.file = file
		self.version_number = version_number

	def get_id(self):
		return self.id

	def get_file(self):
		return self.file

	def set_file(self, file):
		self.file = file

	def get_version_number(self):
		return self.version_number

	def set_version_number(self, version_number):
		self.version_number = version_number

	def get_timestamp(self):
		return self.timestamp
