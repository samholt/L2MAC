class Contact:
	def __init__(self, name, email, phone, block_status=False):
		self.name = name
		self.email = email
		self.phone = phone
		self.block_status = block_status

	def block(self):
		self.block_status = True

	def unblock(self):
		self.block_status = False
