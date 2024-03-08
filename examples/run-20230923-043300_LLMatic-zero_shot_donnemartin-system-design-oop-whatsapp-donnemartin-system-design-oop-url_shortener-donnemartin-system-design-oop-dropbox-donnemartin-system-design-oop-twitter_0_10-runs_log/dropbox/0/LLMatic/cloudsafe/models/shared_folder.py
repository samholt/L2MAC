import sqlite3
from dataclasses import dataclass
from typing import List
from .user import User
from .folder import Folder

@dataclass
class SharedFolder:
	id: int
	users: List[User]
	permissions: List[str]
	folder: Folder

	def invite_user(self, user):
		# Implement logic to invite a user to the shared folder
		pass

	def set_permissions(self, user, permissions):
		# Implement logic to set permissions for a user
		pass
