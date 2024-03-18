import pytest
from recommendation import Recommendation

def test_recommend_users():
	rec = Recommendation()
	rec.users = {1: 'User1', 2: 'User2', 3: 'User3'}
	rec.interests = {1: ['music', 'sports'], 2: ['music'], 3: ['sports']}
	rec.activities = {1: ['post1', 'post2'], 2: ['post3'], 3: ['post4']}
	rec.followers = {1: [2], 2: [1], 3: []}
	assert rec.recommend_users(1) == [2, 3]
	assert rec.recommend_users(2) == [1]
	assert rec.recommend_users(3) == [1]
