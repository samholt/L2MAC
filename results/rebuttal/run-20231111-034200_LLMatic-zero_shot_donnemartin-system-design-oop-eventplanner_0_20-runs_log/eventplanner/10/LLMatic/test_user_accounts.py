import user_accounts

def test_user_profile():
	user_accounts.create_user('John Doe', 'john.doe@example.com', 'Birthday Party')
	profile = user_accounts.view_user('john.doe@example.com')
	assert profile['name'] == 'John Doe'
	assert profile['email'] == 'john.doe@example.com'
	assert profile['preferences'] == 'Birthday Party'

	user_accounts.update_user('john.doe@example.com', 'John Doe', 'Wedding')
	updated_profile = user_accounts.view_user('john.doe@example.com')
	assert updated_profile['preferences'] == 'Wedding'

	user_accounts.save_user_event('john.doe@example.com', 'Event 1', 'past')
	user_accounts.save_user_event('john.doe@example.com', 'Event 2', 'upcoming')
	events = user_accounts.get_user_events('john.doe@example.com', 'past')
	assert 'Event 1' in events
	events = user_accounts.get_user_events('john.doe@example.com', 'upcoming')
	assert 'Event 2' in events
