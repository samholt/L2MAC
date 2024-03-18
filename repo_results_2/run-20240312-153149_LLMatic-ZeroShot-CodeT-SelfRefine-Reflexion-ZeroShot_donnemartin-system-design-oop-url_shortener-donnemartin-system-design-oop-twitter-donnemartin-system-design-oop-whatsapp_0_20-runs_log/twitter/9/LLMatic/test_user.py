import pytest
from user import User

def test_register():
	user = User()
	assert user.register('test@test.com', 'testuser', 'testpass') == True
	assert user.register('test@test.com', 'testuser', 'testpass') == False

def test_authenticate():
	user = User()
	user.register('test@test.com', 'testuser', 'testpass')
	assert user.authenticate('testuser', 'testpass') == True
	assert user.authenticate('testuser', 'wrongpass') == False

def test_reset_password():
	user = User()
	user.register('test@test.com', 'testuser', 'testpass')
	assert user.reset_password('testuser', 'testpass', 'newpass') == True
	assert user.reset_password('testuser', 'wrongpass', 'newpass') == False
	assert user.authenticate('testuser', 'newpass') == True

def test_edit_profile():
	user = User()
	user.register('test@test.com', 'testuser', 'testpass')
	assert user.edit_profile('testuser', 'newpic.jpg', 'This is a bio', 'www.test.com', 'Test City') == True
	assert user.users['testuser']['profile_picture'] == 'newpic.jpg'
	assert user.users['testuser']['bio'] == 'This is a bio'
	assert user.users['testuser']['website_link'] == 'www.test.com'
	assert user.users['testuser']['location'] == 'Test City'

def test_toggle_privacy():
	user = User()
	user.register('test@test.com', 'testuser', 'testpass')
	assert user.toggle_privacy('testuser') == True
	assert user.users['testuser']['is_private'] == True
	assert user.toggle_privacy('testuser') == True
	assert user.users['testuser']['is_private'] == False

def test_follow_unfollow():
	user = User()
	user.register('test1@test.com', 'testuser1', 'testpass')
	user.register('test2@test.com', 'testuser2', 'testpass')
	assert user.follow_user('testuser1', 'testuser2') == True
	assert 'testuser2' in user.users['testuser1']['following']
	assert 'testuser1' in user.users['testuser2']['followers']
	assert user.unfollow_user('testuser1', 'testuser2') == True
	assert 'testuser2' not in user.users['testuser1']['following']
	assert 'testuser1' not in user.users['testuser2']['followers']

def test_get_timeline():
	user = User()
	user.register('test1@test.com', 'testuser1', 'testpass')
	user.register('test2@test.com', 'testuser2', 'testpass')
	user.users['testuser2']['posts'].append('Hello world!')
	user.follow_user('testuser1', 'testuser2')
	assert user.get_timeline('testuser1') == ['Hello world!']
