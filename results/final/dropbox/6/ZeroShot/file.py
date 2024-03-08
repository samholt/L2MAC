from dataclasses import dataclass

@dataclass
class File:
	name: str
	type: str
	size: int
	content: str

	def to_dict(self):
		return {'name': self.name, 'type': self.type, 'size': self.size, 'content': self.content}
