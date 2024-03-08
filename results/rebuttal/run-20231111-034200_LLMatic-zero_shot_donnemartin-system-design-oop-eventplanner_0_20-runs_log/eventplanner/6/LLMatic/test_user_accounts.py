import user_accounts

def test_user_creation():
	user = user_accounts.User('John Doe', 'Rock', [])
	assert user.name == 'John Doe'
	assert user.preferences == 'Rock'
	assert user.events == []

def test_profile_creation():
	user = user_accounts.User('John Doe', 'Rock', [])
	user.create_profile('Jane Doe', 'Pop')
	assert user.name == 'Jane Doe'
	assert user.preferences == 'Pop'

def test_profile_customization():
	user = user_accounts.User('John Doe', 'Rock', [])
	user.customize_profile(preferences='Jazz')
	assert user.preferences == 'Jazz'

def test_event_saving():
	user = user_accounts.User('John Doe', 'Rock', [])
	user.save_event('Event1')
	assert 'Event1' in user.events

def test_event_accessing():
	user = user_accounts.User('John Doe', 'Rock', ['Event1'])
	assert user.access_event('Event1') == 'Event1'

