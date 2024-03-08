class Support:
	def __init__(self):
		self.faq = {}
		self.guides = {}
		self.email_support = 'support@ourapp.com'
		self.phone_support = '+1-800-123-4567'

	def add_faq(self, question, answer):
		self.faq[question] = answer

	def get_faq(self, question):
		return self.faq.get(question, 'Question not found in FAQ.')

	def add_guide(self, title, content):
		self.guides[title] = content

	def get_guide(self, title):
		return self.guides.get(title, 'Guide not found.')

	def get_email_support(self):
		return self.email_support

	def get_phone_support(self):
		return self.phone_support
