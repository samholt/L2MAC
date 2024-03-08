import pytest
from support import Support

def test_handle_chat():
	support = Support()
	assert support.handle_chat('user1', 'Hello') == 'Message received. We will get back to you soon.'
	assert 'user1' in support.chat_logs
	assert support.chat_logs['user1'] == ['Hello']

def test_provide_faq():
	support = Support()
	assert support.provide_faq() == support.faq

def test_provide_user_guide():
	support = Support()
	assert support.provide_user_guide() == support.user_guides

def test_handle_email_support():
	support = Support()
	assert support.handle_email_support('user1', 'user1@example.com') == 'Email received. We will get back to you soon.'
	assert 'user1' in support.email_support
	assert support.email_support['user1'] == 'user1@example.com'

def test_handle_phone_support():
	support = Support()
	assert support.handle_phone_support('user1', '1234567890') == 'Phone number received. We will get back to you soon.'
	assert 'user1' in support.phone_support
	assert support.phone_support['user1'] == '1234567890'
