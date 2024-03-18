from dataclasses import dataclass
from typing import Dict
import uuid

@dataclass
class User:
	id: str
	email: str
	password: str

	def __init__(self, email: str, password: str):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password

	def to_dict(self) -> Dict:
		return {'id': self.id, 'email': self.email}
