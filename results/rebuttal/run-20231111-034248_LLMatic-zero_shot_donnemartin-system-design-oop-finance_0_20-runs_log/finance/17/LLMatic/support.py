class Support:
	def __init__(self):
		self.chat_logs = {}
		self.faq = {}
		self.user_guides = {}
		self.email_support = {}
		self.phone_support = {}

	def handle_chat(self, user_id, message):
		if user_id not in self.chat_logs:
			self.chat_logs[user_id] = []
		self.chat_logs[user_id].append(message)
		return 'Message received. We will get back to you soon.'

	def provide_faq(self):
		return self.faq

	def provide_user_guide(self):
		return self.user_guides

	def handle_email_support(self, user_id, email):
		self.email_support[user_id] = email
		return 'Email received. We will get back to you soon.'

	def handle_phone_support(self, user_id, phone):
		self.phone_support[user_id] = phone
		return 'Phone number received. We will get back to you soon.'
