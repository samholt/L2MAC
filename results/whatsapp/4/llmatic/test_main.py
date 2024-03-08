import main


def test_main():
	app = main.WebApp()
	app.handle_user_interaction('create user testuser testpassword')
	assert 'testuser' in [user.username for user in app.users]
	app.handle_user_interaction('send message testuser receiver Hello')
	assert 'Hello' in [message.content for chat in app.chats for message in chat.messages]
	app.handle_user_interaction('create group testgroup testpicture testuser')
	assert 'testgroup' in [group.name for group in app.groups]
	app.handle_user_interaction('post status testuser testimage public')
	assert 'testimage' in [status.image for status in app.statuses]
