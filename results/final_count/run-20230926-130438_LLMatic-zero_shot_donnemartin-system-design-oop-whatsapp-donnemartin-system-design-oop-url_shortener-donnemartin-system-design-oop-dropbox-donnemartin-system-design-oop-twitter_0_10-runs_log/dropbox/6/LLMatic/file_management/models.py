from dataclasses import dataclass

@dataclass
class File:
	name: str
	file_type: str
	size: int
	content: bytes
	version: int

	def increment_version(self):
		self.version += 1

@dataclass
class Folder:
	name: str
	files: dict

