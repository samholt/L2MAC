class ContactService:
	def __init__(self):
		self.users = {}

	def block_contact(self, user_id, contact_id):
		if user_id not in self.users:
			self.users[user_id] = {'blocked': []}
		if contact_id not in self.users[user_id]['blocked']:
			self.users[user_id]['blocked'].append(contact_id)
		return True

	def unblock_contact(self, user_id, contact_id):
		if user_id in self.users and contact_id in self.users[user_id]['blocked']:
			self.users[user_id]['blocked'].remove(contact_id)
		return True
