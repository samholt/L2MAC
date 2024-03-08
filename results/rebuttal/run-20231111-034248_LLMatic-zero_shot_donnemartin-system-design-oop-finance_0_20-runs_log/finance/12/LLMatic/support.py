class Support:
	def __init__(self):
		self.faq = {
			'How to create an account?': 'Go to the sign up page and fill in the required details.',
			'How to reset my password?': 'Click on the forgot password link on the login page.',
			'How to contact customer support?': 'You can contact us via email at support@ourapp.com or call us at 123-456-7890.'
		}
		self.user_guides = {
			'Account Creation Guide': 'This guide will walk you through the process of creating an account.',
			'Password Reset Guide': 'This guide will help you reset your password if you forget it.',
			'Customer Support Guide': 'This guide will show you how to contact our customer support team.'
		}
		self.email_support = 'support@ourapp.com'
		self.phone_support = '123-456-7890'

	def get_faq(self):
		return self.faq

	def get_user_guides(self):
		return self.user_guides

	def get_email_support(self):
		return self.email_support

	def get_phone_support(self):
		return self.phone_support
