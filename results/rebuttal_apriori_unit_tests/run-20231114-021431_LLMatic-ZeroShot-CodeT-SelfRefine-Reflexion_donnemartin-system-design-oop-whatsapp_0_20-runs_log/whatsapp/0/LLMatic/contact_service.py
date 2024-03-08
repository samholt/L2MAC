class ContactService:
	def __init__(self):
		self.blocked_contacts = {}

	def block_contact(self, user_id, contact_id):
		if user_id not in self.blocked_contacts:
			self.blocked_contacts[user_id] = []
		self.blocked_contacts[user_id].append(contact_id)
		return True

	def unblock_contact(self, user_id, contact_id):
		if user_id in self.blocked_contacts and contact_id in self.blocked_contacts[user_id]:
			self.blocked_contacts[user_id].remove(contact_id)
		return True
