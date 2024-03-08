import pytest
from webapp import WebApp


def test_handle_user_interaction():
	webapp = WebApp()

	# Test user creation
	webapp.handle_user_interaction('create user testuser')
	assert len(webapp.users) == 1
	assert webapp.users[0].username == 'testuser'

	# Test message sending
	webapp.handle_user_interaction('send message testuser testreceiver testcontent')
	assert len(webapp.chats) == 1
	assert webapp.chats[0].messages[0].content == 'testcontent'

	# Test group creation
	webapp.handle_user_interaction('create group testgroup testpicture testadmin')
	assert len(webapp.groups) == 1
	assert webapp.groups[0].name == 'testgroup'

	# Test status posting
	webapp.handle_user_interaction('post status testuser testimage public')
	assert len(webapp.statuses) == 1
	assert webapp.statuses[0].image == 'testimage'

	# Test unknown interaction
	with pytest.raises(Exception):
		webapp.handle_user_interaction('unknown interaction')
