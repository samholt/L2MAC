from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class File:
	name: str
	type: str
	size: int
	content: bytes
	version: int
	preview: str

@dataclass
class Folder:
	name: str
	files: Dict[str, List[File]]
	shared_users: List[str] = field(default_factory=list)

mock_db = {}

MAX_FILE_SIZE = 1000000  # 1MB
ALLOWED_FILE_TYPES = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

def upload_file(file: File) -> str:
	if file.size > MAX_FILE_SIZE:
		return 'File size exceeds limit'
	if file.type not in ALLOWED_FILE_TYPES:
		return 'File type not allowed'
	# Generate a simple preview for the file
	file.preview = file.content[:100]
	if file.name in mock_db:
		mock_db[file.name].append(file)
	else:
		mock_db[file.name] = [file]
	return 'File uploaded successfully'

def download_file(file_name: str) -> File:
	file_versions = mock_db.get(file_name, None)
	if file_versions is None:
		return 'File not found'
	return file_versions[-1]

# Rest of the functions remain the same
