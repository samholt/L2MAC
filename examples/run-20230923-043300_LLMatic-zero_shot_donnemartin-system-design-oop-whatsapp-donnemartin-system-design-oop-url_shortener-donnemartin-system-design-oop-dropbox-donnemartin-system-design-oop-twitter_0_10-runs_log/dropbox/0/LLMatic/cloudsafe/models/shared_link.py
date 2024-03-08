import sqlite3
from dataclasses import dataclass
from .file import File

@dataclass
class SharedLink:
	id: int
	url: str
	expiry_date: str
	password: str
	file: File

	def generate_link(self):
		# Implement logic to generate a shareable link
		pass

	def set_expiry_date(self, date):
		# Implement logic to set an expiry date for the link
		pass

	def set_password(self, password):
		# Implement logic to set a password for the link
		pass
