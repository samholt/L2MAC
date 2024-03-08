class Support:
	def __init__(self):
		self.faq = {}
		self.guides = {}
		self.email_support = ''
		self.phone_support = ''

	def add_faq(self, question, answer):
		self.faq[question] = answer

	def add_guide(self, title, content):
		self.guides[title] = content

	def set_email_support(self, email):
		self.email_support = email

	def set_phone_support(self, phone):
		self.phone_support = phone

	def get_faq(self):
		return self.faq

	def get_guides(self):
		return self.guides

	def get_email_support(self):
		return self.email_support

	def get_phone_support(self):
		return self.phone_support
