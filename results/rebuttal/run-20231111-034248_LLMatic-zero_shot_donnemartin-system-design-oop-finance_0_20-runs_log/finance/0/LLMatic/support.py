class Support:
	def __init__(self):
		self.faq = {
			'How to create an account?': 'Go to the sign up page and fill in the form.',
			'How to reset my password?': 'Click on the forgot password link on the login page.',
			'How to contact customer support?': 'You can contact us via email at support@ourapp.com or call us at 123-456-7890.'
		}
		self.user_guides = {
			'Getting Started': 'This guide will help you get started with our app.',
			'Account Management': 'This guide will help you manage your account settings.',
			'Using Features': 'This guide will help you understand how to use the features of our app.'
		}

	def get_faq(self):
		return self.faq

	def get_user_guide(self, guide):
		return self.user_guides.get(guide, 'Guide not found.')

	def contact_support(self, method):
		if method == 'email':
			return 'Email sent to support@ourapp.com'
		elif method == 'phone':
			return 'Call made to 123-456-7890'
		else:
			return 'Invalid contact method.'
