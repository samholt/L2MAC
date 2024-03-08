from typing import List, Dict
from models.user import User

class ContactManager:
	def __init__(self):
		self.groups = {}

	def block_contact(self, user: User, contact: User):
		if contact.id not in user.blocked_contacts:
			user.blocked_contacts.append(contact.id)

	def unblock_contact(self, user: User, contact: User):
		if contact.id in user.blocked_contacts:
			user.blocked_contacts.remove(contact.id)

	def create_group(self, group_name: str, users: Dict[User, str]):
		self.groups[group_name] = users

	def edit_group(self, group_name: str, users: Dict[User, str]):
		if group_name in self.groups:
			self.groups[group_name] = users

	def manage_group(self, group_name: str, user: User, action: str):
		if group_name in self.groups:
			if action == 'add':
				self.groups[group_name][user] = 'member'
			elif action == 'remove':
				del self.groups[group_name][user]

	def set_admin(self, group_name: str, user: User):
		if group_name in self.groups and user in self.groups[group_name]:
			self.groups[group_name][user] = 'admin'

	def remove_admin(self, group_name: str, user: User):
		if group_name in self.groups and user in self.groups[group_name]:
			self.groups[group_name][user] = 'member'
