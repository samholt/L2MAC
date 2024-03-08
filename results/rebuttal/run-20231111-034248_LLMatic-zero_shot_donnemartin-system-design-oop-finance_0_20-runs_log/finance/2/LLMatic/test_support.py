import pytest
from support import Support

def test_support():
	support = Support()

	# Test FAQ
	support.add_faq('What is this?', 'This is a support system.')
	assert support.get_faq() == {'What is this?': 'This is a support system.'}

	# Test Guides
	support.add_guide('Guide 1', 'This is guide 1.')
	assert support.get_guides() == {'Guide 1': 'This is guide 1.'}

	# Test Chat
	support.add_chat('User1', 'Hello')
	assert support.get_chat() == [('User1', 'Hello')]

	# Test Email Support
	support.set_email_support('support@example.com')
	assert support.get_email_support() == 'support@example.com'

	# Test Phone Support
	support.set_phone_support('1234567890')
	assert support.get_phone_support() == '1234567890'
