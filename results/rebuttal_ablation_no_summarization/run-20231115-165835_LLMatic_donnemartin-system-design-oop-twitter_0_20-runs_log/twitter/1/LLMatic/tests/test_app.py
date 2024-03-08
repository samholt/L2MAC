import pytest
from app import app, User, Post, users, posts

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_trending_topics(client):
	# Clear posts before test
	posts.clear()

	# Create some users
	user1 = User(email='user1@example.com', username='user1', password='password')
	user1.hash_password()
	users[user1.username] = user1
	user2 = User(email='user2@example.com', username='user2', password='password')
	user2.hash_password()
	users[user2.username] = user2
	user3 = User(email='user3@example.com', username='user3', password='password')
	user3.hash_password()
	users[user3.username] = user3

	# Create some posts with hashtags
	post1 = Post(user='user1', text='Hello #world')
	post1.create_post()
	post2 = Post(user='user2', text='Hello #world')
	post2.create_post()
	post3 = Post(user='user3', text='Hello #python')
	post3.create_post()

	# Print out posts for debugging
	print(posts)

	# Check trending topics
	assert Post.trending_topics() == [('#world', 2), ('#python', 1)]


def test_recommend_users_to_follow(client):
	# Clear users before test
	users.clear()

	# Create some users and make them follow each other
	user1 = User(email='user1@example.com', username='user1', password='password')
	user1.hash_password()
	users[user1.username] = user1
	user2 = User(email='user2@example.com', username='user2', password='password')
	user2.hash_password()
	users[user2.username] = user2
	user3 = User(email='user3@example.com', username='user3', password='password')
	user3.hash_password()
	users[user3.username] = user3
	user1.follow('user2')
	user2.follow('user3')

	# Check recommended users to follow for user1
	assert User.recommend_users_to_follow('user1') == ['user3']
