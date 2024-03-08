from user import User


def test_set_online_status():
	user = User('test@test.com', 'password')
	user.set_online_status(True)
	assert user.online == True
	user.set_online_status(False)
	assert user.online == False
