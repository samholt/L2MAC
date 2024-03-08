import user
import datetime

def test_sign_up():
	response = user.sign_up('test@test.com', 'password')
	assert response == 'User created successfully'
	response = user.sign_up('test@test.com', 'password')
	assert response == 'User already exists'

def test_forgot_password():
	response = user.forgot_password('test@test.com')
	assert response == 'Reset link has been sent to your email'
	response = user.forgot_password('nonexistent@test.com')
	assert response == 'User does not exist'

def test_set_profile_picture():
	user_obj = user.User('test@test.com', 'password')
	user_obj.set_profile_picture('profile_pic.jpg')
	assert user_obj.profile_picture == 'profile_pic.jpg'

def test_post_status():
	user_obj = user.User('test@test.com', 'password')
	user_obj.post_status('status.jpg', 24)
	assert user_obj.status == 'status.jpg'
	assert user_obj.status_expiry > datetime.datetime.now()

def test_set_status_visibility():
	user_obj = user.User('test@test.com', 'password')
	user_obj.set_status_visibility('friends')
	assert user_obj.status_visibility == 'friends'

def test_set_privacy_settings():
	user_obj = user.User('test@test.com', 'password')
	user_obj.set_privacy_settings('private')
	assert user_obj.privacy_settings == 'private'

def test_set_online_status():
	user_obj = user.User('test@test.com', 'password')
	user_obj.set_online_status(True)
	assert user_obj.online_status == True
	user_obj.set_online_status(False)
	assert user_obj.online_status == False

def test_queue_message():
	user_obj = user.User('test@test.com', 'password')
	user_obj.queue_message('Hello')
	assert user_obj.message_queue == ['Hello']

def test_send_queued_messages():
	user_obj = user.User('test@test.com', 'password')
	user_obj.queue_message('Hello')
	user_obj.set_online_status(True)
	assert user_obj.message_queue == []
