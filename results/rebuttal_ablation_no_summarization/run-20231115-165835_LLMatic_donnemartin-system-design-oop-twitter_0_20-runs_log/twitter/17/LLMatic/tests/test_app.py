import pytest
from app import app, User, Post, Like, Retweet, Reply, Follow, mock_db, post_db, interaction_db, follow_db

@pytest.fixture
def client():
	with app.test_client() as c:
		yield c


def test_register(client):
	resp = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert resp.status_code == 201
	assert 'User registered successfully' in resp.get_json()['message']
	assert isinstance(mock_db['test'], User)


def test_login(client):
	resp = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert resp.status_code == 200
	assert 'token' in resp.get_json()

	resp = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert resp.status_code == 401
	assert 'Invalid username or password' in resp.get_json()['message']


def test_edit_profile(client):
	resp = client.post('/edit_profile', json={'username': 'test', 'profile_picture': 'new_pic.jpg', 'bio': 'new bio', 'website_link': 'new_website.com', 'location': 'new location', 'is_private': True})
	assert resp.status_code == 200
	assert 'Profile updated successfully' in resp.get_json()['message']
	user = mock_db['test']
	assert user.profile_picture == 'new_pic.jpg'
	assert user.bio == 'new bio'
	assert user.website_link == 'new_website.com'
	assert user.location == 'new location'
	assert user.is_private == True


def test_create_post(client):
	resp = client.post('/create_post', json={'username': 'test', 'text': 'This is a test post', 'images': ['test.jpg']})
	assert resp.status_code == 201
	assert 'Post created successfully' in resp.get_json()['message']
	post_id = resp.get_json()['post_id']
	assert isinstance(post_db[post_id], Post)


def test_delete_post(client):
	resp = client.delete('/delete_post', json={'post_id': 0})
	assert resp.status_code == 200
	assert 'Post deleted successfully' in resp.get_json()['message']
	assert 0 not in post_db


def test_like_post(client):
	resp = client.post('/create_post', json={'username': 'test', 'text': 'This is a test post', 'images': ['test.jpg']})
	post_id = resp.get_json()['post_id']
	resp = client.post('/like_post', json={'username': 'test', 'post_id': post_id})
	assert resp.status_code == 201
	assert 'Post liked successfully' in resp.get_json()['message']
	interaction_id = resp.get_json()['interaction_id']
	assert isinstance(interaction_db[interaction_id], Like)


def test_retweet_post(client):
	resp = client.post('/create_post', json={'username': 'test', 'text': 'This is a test post', 'images': ['test.jpg']})
	post_id = resp.get_json()['post_id']
	resp = client.post('/retweet_post', json={'username': 'test', 'post_id': post_id})
	assert resp.status_code == 201
	assert 'Post retweeted successfully' in resp.get_json()['message']
	interaction_id = resp.get_json()['interaction_id']
	assert isinstance(interaction_db[interaction_id], Retweet)


def test_reply_post(client):
	resp = client.post('/create_post', json={'username': 'test', 'text': 'This is a test post', 'images': ['test.jpg']})
	post_id = resp.get_json()['post_id']
	resp = client.post('/reply_post', json={'username': 'test', 'post_id': post_id, 'text': 'This is a reply'})
	assert resp.status_code == 201
	assert 'Post replied successfully' in resp.get_json()['message']
	interaction_id = resp.get_json()['interaction_id']
	assert isinstance(interaction_db[interaction_id], Reply)


def test_follow(client):
	resp = client.post('/register', json={'email': 'test2@test.com', 'username': 'test2', 'password': 'test2'})
	assert resp.status_code == 201
	resp = client.post('/follow', json={'follower_username': 'test', 'followed_username': 'test2'})
	assert resp.status_code == 201
	assert 'User followed successfully' in resp.get_json()['message']
	follow_id = resp.get_json()['follow_id']
	assert isinstance(follow_db[follow_id], Follow)


def test_unfollow(client):
	resp = client.delete('/unfollow', json={'follower_username': 'test', 'followed_username': 'test2'})
	assert resp.status_code == 200
	assert 'User unfollowed successfully' in resp.get_json()['message']
	assert 0 not in follow_db


def test_timeline(client):
	resp = client.post('/create_post', json={'username': 'test2', 'text': 'This is a test post from test2', 'images': ['test2.jpg']})
	resp = client.post('/follow', json={'follower_username': 'test', 'followed_username': 'test2'})
	resp = client.get('/timeline', json={'username': 'test'})
	assert resp.status_code == 200
	timeline_posts = resp.get_json()['timeline_posts']
	assert len(timeline_posts) == 1
	assert timeline_posts[0]['username'] == 'test2'


def test_search(client):
	resp = client.get('/search', json={'keyword': 'test'})
	assert resp.status_code == 200
	results = resp.get_json()
	assert 'test' in results['users']
	assert 1 in results['posts']


def test_filter(client):
	resp = client.get('/filter', json={'filter_type': 'hashtag', 'filter_value': 'test'})
	assert resp.status_code == 200
	results = resp.get_json()
	assert len(results['posts']) == 0

	resp = client.get('/filter', json={'filter_type': 'mention', 'filter_value': 'test'})
	assert resp.status_code == 200
	results = resp.get_json()
	assert len(results['posts']) == 0

	resp = client.get('/filter', json={'filter_type': 'trending', 'filter_value': 'test'})
	assert resp.status_code == 200
	results = resp.get_json()
	assert len(results['posts']) == 0


def test_home(client):
	resp = client.get('/')
	assert resp.data == b'Hello, World!'

