from user import User

def test_user_creation():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	assert user.username == 'testuser'
	assert user.password == 'testpassword'
	assert user.email == 'testemail@test.com'


def test_user_update():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	user.update_user(username='updateduser', password='updatedpassword', email='updatedemail@test.com')
	assert user.username == 'updateduser'
	assert user.password == 'updatedpassword'
	assert user.email == 'updatedemail@test.com'


def test_user_deletion():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	user.delete_user()
	assert user.username == None
	assert user.password == None
	assert user.email == None


def test_follow_unfollow():
	user1 = User('user1', 'password1', 'email1@test.com')
	user2 = User('user2', 'password2', 'email2@test.com')
	user1.follow_user(user2)
	assert user2 in user1.following
	user1.unfollow_user(user2)
	assert user2 not in user1.following


def test_view_followed_users_reading_lists():
	user1 = User('user1', 'password1', 'email1@test.com')
	user2 = User('user2', 'password2', 'email2@test.com')
	user1.follow_user(user2)
	user2.reading_list = ['book1', 'book2']
	assert user1.view_followed_users_reading_lists() == {'user2': ['book1', 'book2']}


def test_view_followed_users_recommendations():
	user1 = User('user1', 'password1', 'email1@test.com')
	user2 = User('user2', 'password2', 'email2@test.com')
	user1.follow_user(user2)
	user2.recommendations = ['book3', 'book4']
	assert user1.view_followed_users_recommendations() == {'user2': ['book3', 'book4']}


def test_add_remove_reading_list():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	user.add_to_reading_list('book1')
	assert 'book1' in user.reading_list
	user.remove_from_reading_list('book1')
	assert 'book1' not in user.reading_list


def test_add_remove_recommendations():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	user.add_recommendation('book2')
	assert 'book2' in user.recommendations
	user.remove_recommendation('book2')
	assert 'book2' not in user.recommendations
