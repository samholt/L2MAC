from dataclasses import dataclass

@dataclass
class FileManager:
	file: dict
	user_email: str

	def to_dict(self):
		return {'file': self.file, 'user_email': self.user_email}
