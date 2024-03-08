from dataclasses import dataclass
from cloudsafe.models.file import File
from cloudsafe.models.folder import Folder


@dataclass
class SharedLink:
	id: str
	item: [File, Folder]
	expiry_date: str
	password: str = None

	def __init__(self, item, expiry_date, password=None):
		self.id = item.id
		self.item = item
		self.expiry_date = expiry_date
		self.password = password
