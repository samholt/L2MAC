import pytest
from user import User
from post import Post


def test_register():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.register() == user


def test_authenticate():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.authenticate('testpassword') is not None
	assert user.authenticate('wrongpassword') is None


def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.reset_password('newpassword')
	assert user.password == 'newpassword'


def test_set_profile_picture():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.set_profile_picture('picture.jpg')
	assert user.profile_picture == 'picture.jpg'


def test_set_bio():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.set_bio('This is a bio')
	assert user.bio == 'This is a bio'


def test_set_website_link():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.set_website_link('www.example.com')
	assert user.website_link == 'www.example.com'


def test_set_location():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.set_location('New York')
	assert user.location == 'New York'


def test_toggle_privacy():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_follow():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	assert user1.follow(user2) == 'Followed'
	assert user2 in user1.following
	assert user1 in user2.followers
	assert f'{user1.username} started following you' in user2.notifications


def test_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	user1.follow(user2)
	assert user1.unfollow(user2) == 'Unfollowed'
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_view_timeline():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword3', False)
	user1.follow(user2)
	user1.follow(user3)
	post1 = Post(user2, 'post1')
	post2 = Post(user2, 'post2')
	post3 = Post(user3, 'post3')
	post4 = Post(user3, 'post4')
	user2.posts = [post1, post2]
	user3.posts = [post3, post4]
	assert sorted([post.content for post in user1.view_timeline()], reverse=True) == sorted([post1.content, post2.content, post3.content, post4.content], reverse=True)


def test_view_notifications():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	user1.follow(user2)
	assert user2.view_notifications() == [f'{user1.username} started following you']


def test_receive_like_notification():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	post = Post(user1, 'post')
	user2.receive_like_notification(post)
	assert f'{user1.username} liked your post: {post.content}' in user2.notifications


def test_receive_retweet_notification():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	post = Post(user1, 'post')
	user2.receive_retweet_notification(post)
	assert f'{user1.username} retweeted your post: {post.content}' in user2.notifications


def test_receive_reply_notification():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	post = Post(user1, 'post')
	reply = Post(user2, 'reply')
	user1.receive_reply_notification(post, reply)
	assert f'{user2.username} replied to your post: {post.content}' in user1.notifications


def test_receive_mention_notification():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	post = Post(user1, 'post')
	user2.receive_mention_notification(post)
	assert f'{user1.username} mentioned you in a post: {post.content}' in user2.notifications


def test_recommend_users():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword3', False)
	user4 = User('test4@test.com', 'testuser4', 'testpassword4', False)
	user1.follow(user2)
	user2.follow(user1)
	user3.follow(user1)
	user4.follow(user2)
	user4.follow(user3)
	user1.follow(user4)
	user4.follow(user1)
	user2.posts = [Post(user2, 'post1'), Post(user2, 'post2')]
	user3.posts = [Post(user3, 'post3')]
	user4.posts = [Post(user4, 'post4'), Post(user4, 'post5'), Post(user4, 'post6')]
	assert set([user.username for user in user1.recommend_users([user2, user3, user4])]) == set([user2.username, user3.username])

