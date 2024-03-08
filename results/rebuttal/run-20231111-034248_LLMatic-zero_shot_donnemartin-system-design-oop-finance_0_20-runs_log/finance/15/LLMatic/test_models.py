import models

def test_user():
	user = models.User('test', 'test', 'test@test.com')
	assert user.username == 'test'
	assert user.password == 'test'
	assert user.email == 'test@test.com'

	user.create_user('test2', 'test2', 'test2@test.com')
	assert user.user_data['test2'] == {'password': 'test2', 'email': 'test2@test.com'}

	user.update_user('test2', password='newtest2', email='newtest2@test.com')
	assert user.user_data['test2'] == {'password': 'newtest2', 'email': 'newtest2@test.com'}

	user.delete_user('test2')
	assert 'test2' not in user.user_data
