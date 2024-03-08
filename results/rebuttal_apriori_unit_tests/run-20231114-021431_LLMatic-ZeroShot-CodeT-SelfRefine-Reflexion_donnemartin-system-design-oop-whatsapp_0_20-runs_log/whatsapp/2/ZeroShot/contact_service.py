class ContactService:
	def __init__(self):
		self.contacts = {}

	def block_contact(self, user_id, contact_id):
		if user_id not in self.contacts:
			self.contacts[user_id] = {'blocked': []}
		self.contacts[user_id]['blocked'].append(contact_id)
		return True

	def unblock_contact(self, user_id, contact_id):
		if user_id not in self.contacts or contact_id not in self.contacts[user_id]['blocked']:
			return False
		self.contacts[user_id]['blocked'].remove(contact_id)
		return True
