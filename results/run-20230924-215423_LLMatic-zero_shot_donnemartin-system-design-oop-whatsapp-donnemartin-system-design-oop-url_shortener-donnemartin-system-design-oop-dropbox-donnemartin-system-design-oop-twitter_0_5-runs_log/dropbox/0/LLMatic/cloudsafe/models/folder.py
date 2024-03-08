from dataclasses import dataclass

@dataclass
class Folder:
	id: str
	name: str
	parent_folder: str
