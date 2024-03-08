import pytest
from user import User
from post import Post


def test_register():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.register() == 'User registered successfully'


def test_authenticate():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert 'Invalid password' == user.authenticate('wrongpassword')
	assert isinstance(user.authenticate('testpassword'), str)


def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.reset_password('newpassword')
	assert 'Invalid password' == user.authenticate('testpassword')
	assert isinstance(user.authenticate('newpassword'), str)


def test_update_profile_picture():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.update_profile_picture('new_picture.jpg')
	assert user.profile_picture == 'new_picture.jpg'


def test_update_bio():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.update_bio('New bio')
	assert user.bio == 'New bio'


def test_update_website_link():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.update_website_link('www.newwebsite.com')
	assert user.website_link == 'www.newwebsite.com'


def test_update_location():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.update_location('New location')
	assert user.location == 'New location'


def test_toggle_privacy():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_follow_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	assert user1.follow(user2) == 'Followed successfully'
	assert user2 in user1.following
	assert user1 in user2.followers
	assert f'{user1.username} started following you.' in user2.notifications
	assert user1.unfollow(user2) == 'Unfollowed successfully'
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_view_timeline():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user1.follow(user2)
	post1 = Post(user2, 'Post1')
	post2 = Post(user2, 'Post2')
	user2.posts = [post1, post2]
	assert user1.view_timeline() == [post2, post1]


def test_receive_notification():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.receive_notification('New notification')
	assert 'New notification' in user.notifications


def test_like_post():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	post = Post(user, 'Post')
	assert user.like_post(post) == 'Post liked successfully'
	assert post in user.likes


def test_recommend_users():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword', False)
	user4 = User('test4@test.com', 'testuser4', 'testpassword', False)
	users = [user1, user2, user3, user4]
	# User2 and User3 like the same post as User1
	post = Post(user1, 'Post')
	user1.like_post(post)
	user2.like_post(post)
	user3.like_post(post)
	# User4 has more posts than User1
	post1 = Post(user4, 'Post1')
	post2 = Post(user4, 'Post2')
	user4.posts = [post1, post2]
	# User2 and User3 follow User4
	user2.follow(user4)
	user3.follow(user4)
	recommendations = user1.recommend_users(users)
	assert user2 in recommendations
	assert user3 in recommendations
	assert user4 in recommendations

