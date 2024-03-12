import pytest
from models import User, Follow, Post, db
from app import create_app


@pytest.fixture
def client():
	app = create_app({'TESTING': True})
	with app.app_context():
		db.create_all()
		user1 = User(username='user1', email='user1@example.com', password='password')
		user2 = User(username='user2', email='user2@example.com', password='password')
		db.session.add(user1)
		db.session.add(user2)
		db.session.commit()
		with app.test_client() as client:
			yield client
		db.session.remove()
		db.drop_all()

def test_follow_user(client):
	user1 = User.query.filter_by(username='user1').first()
	user2 = User.query.filter_by(username='user2').first()

	response = client.post('/follow_user/' + str(user2.id), headers={'Authorization': 'Bearer ' + user1.access_token})

	assert response.status_code == 200
	assert response.get_json()['message'] == 'User followed'

	follow = Follow.query.filter_by(follower_id=user1.id, followed_id=user2.id).first()

	assert follow is not None

def test_unfollow_user(client):
	user1 = User.query.filter_by(username='user1').first()
	user2 = User.query.filter_by(username='user2').first()
	follow = Follow(follower_id=user1.id, followed_id=user2.id)
	db.session.add(follow)
	db.session.commit()

	response = client.post('/unfollow_user/' + str(user2.id), headers={'Authorization': 'Bearer ' + user1.access_token})

	assert response.status_code == 200
	assert response.get_json()['message'] == 'User unfollowed'

	follow = Follow.query.filter_by(follower_id=user1.id, followed_id=user2.id).first()

	assert follow is None

def test_view_followers(client):
	user1 = User.query.filter_by(username='user1').first()
	user2 = User.query.filter_by(username='user2').first()
	follow = Follow(follower_id=user1.id, followed_id=user2.id)
	db.session.add(follow)
	db.session.commit()

	response = client.get('/view_followers/' + str(user2.id))

	assert response.status_code == 200
	assert 'user1' in response.get_json()['followers']

def test_view_following(client):
	user1 = User.query.filter_by(username='user1').first()
	user2 = User.query.filter_by(username='user2').first()
	follow = Follow(follower_id=user1.id, followed_id=user2.id)
	db.session.add(follow)
	db.session.commit()

	response = client.get('/view_following/' + str(user1.id))

	assert response.status_code == 200
	assert 'user2' in response.get_json()['following']

def test_view_timeline(client):
	user1 = User.query.filter_by(username='user1').first()
	user2 = User.query.filter_by(username='user2').first()
	follow = Follow(follower_id=user1.id, followed_id=user2.id)
	post = Post(content='Hello, world!', user_id=user2.id)
	db.session.add(follow)
	db.session.add(post)
	db.session.commit()

	response = client.get('/view_timeline', headers={'Authorization': 'Bearer ' + user1.access_token})

	assert response.status_code == 200
	assert 'Hello, world!' in response.get_json()['posts']
