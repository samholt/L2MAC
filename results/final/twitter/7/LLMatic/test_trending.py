import pytest
import trending
from database import trends_db, users_db, follows_db

def test_trending():
	response = trending.trending()
	assert response[1] == 200
	assert 'trends' in response[0]

	# Check if trends are sorted by mentions
	trends = response[0]['trends']
	for i in range(len(trends) - 1):
		assert trends[i]['mentions'] >= trends[i + 1]['mentions']

def test_recommendations():
	# Add test data
	users_db['test1'] = {'user_id': 'test1'}
	users_db['test2'] = {'user_id': 'test2'}
	follows_db['test1'] = {'follower_id': 'test1', 'followee_id': 'test2'}

	response = trending.recommendations('test1')
	assert response[1] == 200
	assert 'recommendations' in response[0]

	# Check if recommendations are sorted by mutual followers
	recommendations = response[0]['recommendations']
	for i in range(len(recommendations) - 1):
		assert len([follow for follow in follows_db.values() if follow['followee_id'] == recommendations[i]['user_id']]) >= len([follow for follow in follows_db.values() if follow['followee_id'] == recommendations[i + 1]['user_id']])
