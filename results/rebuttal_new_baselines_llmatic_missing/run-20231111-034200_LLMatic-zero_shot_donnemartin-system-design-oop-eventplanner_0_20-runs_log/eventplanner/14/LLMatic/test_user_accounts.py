import user_accounts

def test_create_profile():
	user = user_accounts.User('John Doe', [], [])
	user.create_profile('John Doe', ['Music', 'Art'])
	assert user.name == 'John Doe'
	assert user.preferences == ['Music', 'Art']

def test_update_profile():
	user = user_accounts.User('John Doe', [], [])
	user.update_profile('John Doe', ['Sports', 'Travel'])
	assert user.name == 'John Doe'
	assert user.preferences == ['Sports', 'Travel']

def test_save_and_get_events():
	user = user_accounts.User('John Doe', [], [])
	event = {'name': 'Music Festival', 'date': '2022-12-31'}
	user.save_event(event)
	assert user.get_events() == [event]
