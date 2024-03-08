from dataclasses import dataclass

@dataclass
class User:
	id: int
	name: str
	email: str
	password: str

	def save(self):
		# Mock save method
		pass

	def to_dict(self):
		# Convert to dictionary
		return {'id': self.id, 'name': self.name, 'email': self.email, 'password': self.password}

@dataclass
class File:
	id: int
	name: str
	user_id: int
	folder_id: int
	version: int

	def save(self):
		# Mock save method
		pass

	def to_dict(self):
		# Convert to dictionary
		return {'id': self.id, 'name': self.name, 'user_id': self.user_id, 'folder_id': self.folder_id, 'version': self.version}

@dataclass
class Folder:
	id: int
	name: str
	user_id: int

	def save(self):
		# Mock save method
		pass

	def to_dict(self):
		# Convert to dictionary
		return {'id': self.id, 'name': self.name, 'user_id': self.user_id}

@dataclass
class ActivityLog:
	user_id: int
	action: str

	def save(self):
		# Mock save method
		pass

	def to_dict(self):
		# Convert to dictionary
		return {'user_id': self.user_id, 'action': self.action}
