import pytest
from user import User
from chat import Chat
from message import Message
from webapp import WebApp


def test_display_status():
	webapp = WebApp()
	webapp.register_user('test@test.com', 'password')
	assert webapp.display_status('test@test.com') == False
	webapp.login_user('test@test.com', 'password')
	assert webapp.display_status('test@test.com') == True


def test_restore_connectivity():
	webapp = WebApp()
	webapp.register_user('test@test.com', 'password')
	webapp.register_user('test2@test.com', 'password')
	webapp.send_message('test@test.com', 'test2@test.com', 'Hello!', 'text')
	assert len(webapp.chats[0].offline_messages) == 1
	webapp.restore_connectivity('test2@test.com')
	assert len(webapp.chats[0].offline_messages) == 0
	assert len(webapp.chats[0].messages) == 1
