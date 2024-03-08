import datetime
from trending import Trending


def test_get_trending_topics():
	trending = Trending()
	timestamp1 = datetime.datetime.now()
	trending.post.create('user1', '#topic1 #topic2', 'image1')
	timestamp2 = datetime.datetime.now()
	trending.post.create('user2', '#topic2 #topic3', 'image2')
	timestamp3 = datetime.datetime.now()
	trending.post.create('user3', '#topic1 #topic3', 'image3')
	assert trending.get_trending_topics() == ['#topic1', '#topic2', '#topic3']


def test_recommend_users():
	trending = Trending()
	trending.post.create('user1', '#topic1 #topic2', 'image1')
	trending.post.create('user2', '#topic2 #topic3', 'image2')
	trending.post.create('user3', '#topic1 #topic3', 'image3')
	assert 'user3' in trending.recommend_users('user1')
