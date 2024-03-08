import main

def test_main():
	main.main()
	assert main.auth.validate_user('user1', 'password1')
	assert main.profile.profile_picture == 'picture.jpg'
	assert 'user2' in main.contacts.contacts
	assert main.messaging.messages[0].content == 'Hello, user2!'
	assert 'group1' in main.groups.groups
	assert main.status.statuses[0] == 'status.jpg'
	assert main.webapp.auth.validate_user('user3', 'password3')
	assert 'user1' in main.connectivity.online_users
