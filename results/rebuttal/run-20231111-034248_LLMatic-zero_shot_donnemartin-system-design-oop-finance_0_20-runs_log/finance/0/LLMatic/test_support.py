import pytest
from support import Support

def test_faq():
	support = Support()
	faq = support.get_faq()
	assert isinstance(faq, dict)
	assert 'How to create an account?' in faq


def test_user_guide():
	support = Support()
	guide = support.get_user_guide('Getting Started')
	assert guide == 'This guide will help you get started with our app.'
	guide = support.get_user_guide('Invalid Guide')
	assert guide == 'Guide not found.'


def test_contact_support():
	support = Support()
	response = support.contact_support('email')
	assert response == 'Email sent to support@ourapp.com'
	response = support.contact_support('phone')
	assert response == 'Call made to 123-456-7890'
	response = support.contact_support('invalid')
	assert response == 'Invalid contact method.'
