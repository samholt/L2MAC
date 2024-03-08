import pytest
import social
from database import users_db, posts_db, follows_db, notifications_db

# Test data
user1 = {'email': 'user1@test.com', 'username': 'user1', 'password': 'password1', 'profile_picture': '', 'bio': '', 'website_link': '', 'location': '', 'is_private': False}
user2 = {'email': 'user2@test.com', 'username': 'user2', 'password': 'password2', 'profile_picture': '', 'bio': '', 'website_link': '', 'location': '', 'is_private': False}
post1 = {'user_id': 'user1@test.com', 'content': 'Hello, world!', 'image': '', 'timestamp': '2022-01-01T00:00:00Z'}
post2 = {'user_id': 'user2@test.com', 'content': 'Hello, world!', 'image': '', 'timestamp': '2022-01-01T00:00:00Z'}
follow1 = {'follower_id': 'user1@test.com', 'followee_id': 'user2@test.com', 'timestamp': '2022-01-01T00:00:00Z'}

# Setup
users_db[user1['email']] = user1
users_db[user2['email']] = user2
posts_db['1'] = post1
posts_db['2'] = post2
follows_db[follow1['follower_id']] = follow1

# Tests

def test_follow():
	response = social.app.test_client().post('/follow', json=follow1)
	assert response.status_code == 201
	assert follows_db[follow1['follower_id']] == follow1
	assert notifications_db[follow1['followee_id']]['content'] == f"{follow1['follower_id']} has started following you."


def test_unfollow():
	response = social.app.test_client().post('/unfollow', json={'follower_id': follow1['follower_id'], 'followee_id': follow1['followee_id']})
	assert response.status_code == 200
	assert follow1['follower_id'] not in follows_db


def test_timeline():
	response = social.app.test_client().get('/timeline', query_string={'user_id': user1['email']})
	assert response.status_code == 200
	assert len(response.get_json()['timeline']) == 1
	assert response.get_json()['timeline'][0]['user_id'] == user2['email']
	assert response.get_json()['timeline'][0]['content'] == post2['content']

