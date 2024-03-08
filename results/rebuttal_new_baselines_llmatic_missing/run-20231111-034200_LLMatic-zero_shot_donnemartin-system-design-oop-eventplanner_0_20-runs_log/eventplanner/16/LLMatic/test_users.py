import users

def test_create_user():
	user = users.create_user('John')
	assert user.name == 'John'
	assert user.preferences == {}
	assert user.events == {'past': [], 'upcoming': []}

def test_update_user():
	user = users.create_user('John')
	users.update_user('John', {'preference1': 'value1'})
	assert user.preferences == {'preference1': 'value1'}

def test_save_user_event():
	user = users.create_user('John')
	users.save_user_event('John', 'event1', 'past')
	assert user.events['past'] == ['event1']

def test_get_user_events():
	user = users.create_user('John')
	users.save_user_event('John', 'event1', 'past')
	assert users.get_user_events('John', 'past') == ['event1']
