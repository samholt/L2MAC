from dataclasses import dataclass
import uuid

@dataclass

class Chat:
	id: str
	name: str

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name
		}
