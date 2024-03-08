import pytest
from support import Support

def test_support_system():
	support = Support()

	# Test FAQ
	support.add_faq('How to use the app?', 'Here is a guide...')
	assert support.get_faq('How to use the app?') == 'Here is a guide...'
	assert support.get_faq('Non-existing question') == 'Question not found in FAQ.'

	# Test Guides
	support.add_guide('User Guide', 'Here is the user guide...')
	assert support.get_guide('User Guide') == 'Here is the user guide...'
	assert support.get_guide('Non-existing guide') == 'Guide not found.'

	# Test Email and Phone Support
	assert support.get_email_support() == 'support@ourapp.com'
	assert support.get_phone_support() == '+1-800-123-4567'
