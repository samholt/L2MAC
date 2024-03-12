import pytest
import bcrypt
from models import User, Post, Like, Retweet, Reply, db
from app import create_app


@pytest.fixture
def client():
	app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:', 'SECRET_KEY': 'secret'})
	with app.test_client() as client:
		with app.app_context():
			# create all tables in the database
			db.create_all()
			# create a user
			password_hash = bcrypt.hashpw('test'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
			user = User(username='test', email='test@test.com', password=password_hash)
			db.session.add(user)
			db.session.commit()
			assert User.query.filter_by(username='test').first() is not None
			# login the user
			response = client.post('/login', json={'username': 'test', 'password': 'test'})
			access_token = response.get_json()['access_token']
			# create a post
			post = Post(content='Test post', user_id=user.id)
			db.session.add(post)
			db.session.commit()
			assert Post.query.filter_by(content='Test post').first() is not None
			# like the post
			like = Like(user_id=user.id, post_id=post.id)
			db.session.add(like)
			db.session.commit()
			assert Like.query.filter_by(user_id=user.id, post_id=post.id).first() is not None
			# retweet the post
			retweet = Retweet(user_id=user.id, post_id=post.id)
			db.session.add(retweet)
			db.session.commit()
			assert Retweet.query.filter_by(user_id=user.id, post_id=post.id).first() is not None
			# reply to the post
			reply = Reply(content='Test reply', user_id=user.id, post_id=post.id)
			db.session.add(reply)
			db.session.commit()
			assert Reply.query.filter_by(user_id=user.id, post_id=post.id).first() is not None
			yield client, access_token, user.id


def test_like_post(client):
	client, access_token, user_id = client
	response = client.post('/like_post/1', headers={'Authorization': 'Bearer ' + access_token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post liked'}
	like = Like.query.filter_by(user_id=user_id, post_id=1).first()
	assert like is not None


def test_retweet_post(client):
	client, access_token, user_id = client
	response = client.post('/retweet_post/1', headers={'Authorization': 'Bearer ' + access_token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post retweeted'}
	retweet = Retweet.query.filter_by(user_id=user_id, post_id=1).first()
	assert retweet is not None


def test_reply_post(client):
	client, access_token, user_id = client
	response = client.post('/reply_post/1', headers={'Authorization': 'Bearer ' + access_token}, json={'content': 'Test reply'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Reply posted'}
	reply = Reply.query.filter_by(user_id=user_id, post_id=1).first()
	assert reply is not None


def test_view_interactions(client):
	client, access_token, user_id = client
	response = client.get('/view_interactions/1')
	assert response.status_code == 200
	json_data = response.get_json()
	assert 'likes' in json_data
	assert 'retweets' in json_data
	assert 'replies' in json_data
	assert json_data['likes'] == 1
	assert json_data['retweets'] == 1
	assert json_data['replies'] == ['Test reply']

