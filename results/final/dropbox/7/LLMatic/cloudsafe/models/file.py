from dataclasses import dataclass

@dataclass
class File:
	id: str
	name: str
	size: int
	type: str
	parent_folder: str
	version_history: list
