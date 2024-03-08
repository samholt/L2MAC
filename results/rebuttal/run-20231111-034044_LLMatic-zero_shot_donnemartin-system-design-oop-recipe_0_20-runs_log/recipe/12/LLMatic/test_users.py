import users

def test_user_creation():
	user = users.create_user('test', 'password')
	assert user.username == 'test'
	assert user.password == 'password'


def test_user_deletion():
	users.create_user('test', 'password')
	users.delete_user('test')
	assert users.get_user('test') is None


def test_favorite_recipes():
	user = users.create_user('test', 'password')
	user.add_favorite_recipe('recipe1')
	assert 'recipe1' in user.favorite_recipes
	user.remove_favorite_recipe('recipe1')
	assert 'recipe1' not in user.favorite_recipes


def test_followed_users():
	user1 = users.create_user('test1', 'password')
	user2 = users.create_user('test2', 'password')
	user1.follow_user(user2)
	assert user2 in user1.followed_users
	user1.unfollow_user(user2)
	assert user2 not in user1.followed_users
