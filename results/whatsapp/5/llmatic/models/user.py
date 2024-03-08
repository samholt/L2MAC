from dataclasses import dataclass
from typing import List

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: dict
	blocked_contacts: List[str]
	online_status: bool = False

	def recover_password(self):
		# Generate a new password
		new_password = 'new_password'
		# Send the new password to the user's email
		# This is a placeholder. In a real application, you would integrate with an email service.
		print(f'Sent new password to {self.email}')
		self.password = new_password

	def __hash__(self):
		return hash(self.id)
