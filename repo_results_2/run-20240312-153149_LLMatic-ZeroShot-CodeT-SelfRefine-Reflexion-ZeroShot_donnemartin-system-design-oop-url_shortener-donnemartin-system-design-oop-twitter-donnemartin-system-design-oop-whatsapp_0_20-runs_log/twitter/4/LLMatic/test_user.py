import pytest
from user import User
from post import Post


def test_register():
	user = User('testuser', 'testpass')
	assert user.username == 'testuser'
	assert user.password == 'testpass'


def test_authenticate():
	user = User('testuser', 'testpass')
	assert user.authenticate('testpass') == True
	assert user.authenticate('wrongpass') == False


def test_reset_password():
	user = User('testuser', 'testpass')
	user.reset_password('newpass')
	assert user.authenticate('newpass') == True


def test_set_profile_picture():
	user = User('testuser', 'testpass')
	user.set_profile_picture('newpic.jpg')
	assert user.profile_picture == 'newpic.jpg'


def test_update_bio():
	user = User('testuser', 'testpass')
	user.update_bio('new bio')
	assert user.bio == 'new bio'


def test_add_website_link():
	user = User('testuser', 'testpass')
	user.add_website_link('newwebsite.com')
	assert user.website_link == 'newwebsite.com'


def test_set_location():
	user = User('testuser', 'testpass')
	user.set_location('new location')
	assert user.location == 'new location'


def test_toggle_privacy():
	user = User('testuser', 'testpass')
	user.toggle_privacy()
	assert user.private == True
	user.toggle_privacy()
	assert user.private == False


def test_follow_unfollow():
	user1 = User('testuser1', 'testpass')
	user2 = User('testuser2', 'testpass')
	user1.follow(user2)
	assert user2 in user1.following
	assert user1 in user2.followers
	user1.unfollow(user2)
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_view_timeline():
	user1 = User('testuser1', 'testpass')
	user2 = User('testuser2', 'testpass')
	user1.follow(user2)
	post = Post('testuser2', 'Hello world!')
	user2.post(post)
	assert len(user1.view_timeline()) == 1


def test_recommend_users():
	user1 = User('testuser1', 'testpass')
	user2 = User('testuser2', 'testpass')
	user3 = User('testuser3', 'testpass')
	user4 = User('testuser4', 'testpass')
	user1.follow(user2)
	user2.follow(user3)
	user3.follow(user4)
	user4.follow(user1)
	post1 = Post('testuser2', 'Hello world!')
	post2 = Post('testuser3', 'Hello world!')
	post3 = Post('testuser4', 'Hello world!')
	user2.post(post1)
	user3.post(post2)
	user4.post(post3)
	all_users = [user1, user2, user3, user4]
	recommendations = user1.recommend_users(all_users)
	assert user4 in recommendations
	assert user3 in recommendations
	assert user2 not in recommendations
	assert recommendations.index(user3) < recommendations.index(user4)

