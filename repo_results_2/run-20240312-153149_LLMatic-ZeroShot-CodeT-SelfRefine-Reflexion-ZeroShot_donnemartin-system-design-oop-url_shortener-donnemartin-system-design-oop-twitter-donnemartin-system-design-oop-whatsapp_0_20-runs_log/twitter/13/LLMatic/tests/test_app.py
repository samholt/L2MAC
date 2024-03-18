import pytest
from app import app, User, Profile, Post, Message, mock_db, post_id
from werkzeug.security import check_password_hash


def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test123'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Registered successfully'}
		user = mock_db.get('test')
		assert user.username == 'test'
		assert user.email == 'test@test.com'
		assert check_password_hash(user.password, 'test123')
		assert isinstance(user.profile, Profile)
		assert user.posts == []
		assert user.followers == []
		assert user.following == []
		assert user.messages == []


def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test123'})
		assert resp.status_code == 200
		assert 'token' in resp.get_json()


def test_profile():
	with app.test_client() as c:
		resp = c.get('/profile/test')
		assert resp.status_code == 200
		assert 'bio' in resp.get_json()
		assert 'website' in resp.get_json()
		assert 'location' in resp.get_json()
		assert 'is_private' in resp.get_json()
		resp = c.put('/profile/test', json={'bio': 'New bio', 'website': 'New website', 'location': 'New location', 'is_private': True})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Profile updated successfully'}
		user = mock_db.get('test')
		assert user.profile.bio == 'New bio'
		assert user.profile.website == 'New website'
		assert user.profile.location == 'New location'
		assert user.profile.is_private == True


def test_follow():
	with app.test_client() as c:
		resp = c.post('/register', json={'username': 'test2', 'email': 'test2@test.com', 'password': 'test123'})
		assert resp.status_code == 200
		resp = c.post('/follow', json={'username': 'test', 'to_follow': 'test2'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Followed successfully'}
		user = mock_db.get('test')
		follow_user = mock_db.get('test2')
		assert follow_user in user.following
		assert user in follow_user.followers


def test_unfollow():
	with app.test_client() as c:
		resp = c.post('/unfollow', json={'username': 'test', 'to_unfollow': 'test2'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Unfollowed successfully'}
		user = mock_db.get('test')
		unfollow_user = mock_db.get('test2')
		assert unfollow_user not in user.following
		assert user not in unfollow_user.followers


def test_feed():
	with app.test_client() as c:
		resp = c.post('/post', json={'username': 'test2', 'content': 'This is a test post', 'images': ['image1.jpg', 'image2.jpg']})
		assert resp.status_code == 200
		resp = c.post('/follow', json={'username': 'test', 'to_follow': 'test2'})
		assert resp.status_code == 200
		resp = c.get('/feed/test')
		assert resp.status_code == 200
		feed = resp.get_json()
		assert len(feed) == 1
		assert {'username': 'test2', 'post_id': post_id + 1, 'content': 'This is a test post'} in feed


def test_message():
	with app.test_client() as c:
		resp = c.post('/message', json={'from_username': 'test', 'to_username': 'test2', 'content': 'Hello, test2'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Message sent successfully'}
		from_user = mock_db.get('test')
		to_user = mock_db.get('test2')
		assert len(from_user.messages) == 1
		assert len(to_user.messages) == 1
		assert from_user.messages[0].content == 'Hello, test2'
		assert to_user.messages[0].content == 'Hello, test2'


def test_messages():
	with app.test_client() as c:
		resp = c.get('/messages/test')
		assert resp.status_code == 200
		messages = resp.get_json()
		assert len(messages) == 1
		assert {'from': 'test', 'to': 'test2', 'content': 'Hello, test2'} in messages


def test_post():
	with app.test_client() as c:
		resp = c.post('/post', json={'username': 'test', 'content': 'This is a test post', 'images': ['image1.jpg', 'image2.jpg']})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Post created successfully'}
		user = mock_db.get('test')
		assert len(user.posts) == 1
		assert user.posts[0].id == post_id + 1
		assert user.posts[0].content == 'This is a test post'
		assert user.posts[0].images == ['image1.jpg', 'image2.jpg']
		assert user.posts[0].likes == 0
		assert user.posts[0].retweets == 0
		assert user.posts[0].replies == []


def test_delete_post():
	with app.test_client() as c:
		resp = c.delete(f'/post/{post_id + 1}')
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Post deleted successfully'}
		user = mock_db.get('test')
		assert len(user.posts) == 0


def test_search():
	with app.test_client() as c:
		resp = c.get('/search?keyword=test')
		assert resp.status_code == 200
		results = resp.get_json()
		assert len(results) == 1
		assert {'type': 'user', 'username': 'test'} in results
		resp = c.get('/search?keyword=nonexistent')
		assert resp.status_code == 200
		assert resp.get_json() == []


def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'

