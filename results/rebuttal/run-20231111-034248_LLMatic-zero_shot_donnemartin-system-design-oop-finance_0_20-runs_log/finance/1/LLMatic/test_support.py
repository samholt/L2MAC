import pytest
from support import Support

def test_support():
	# Initialize support
	support = Support()

	# Add FAQ
	support.add_faq('How to register?', 'Go to registration page and fill the form.')
	assert support.get_faq()['How to register?'] == 'Go to registration page and fill the form.'

	# Add Guide
	support.add_guide('Registration Guide', 'Step 1: Go to registration page.\nStep 2: Fill the form.')
	assert support.get_guides()['Registration Guide'] == 'Step 1: Go to registration page.\nStep 2: Fill the form.'

	# Set email support
	support.set_email_support('support@example.com')
	assert support.get_email_support() == 'support@example.com'

	# Set phone support
	support.set_phone_support('1234567890')
	assert support.get_phone_support() == '1234567890'
