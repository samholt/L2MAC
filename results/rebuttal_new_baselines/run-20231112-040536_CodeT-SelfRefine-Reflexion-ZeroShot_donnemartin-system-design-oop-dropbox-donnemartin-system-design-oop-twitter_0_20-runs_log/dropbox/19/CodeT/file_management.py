from dataclasses import dataclass

@dataclass
class File:
	name: str
	size: int
	type: str
	content: str

files = {}

def upload(data):
	file = File(**data)
	files[file.name] = file
	return file

def download(data):
	return files.get(data['name'])
