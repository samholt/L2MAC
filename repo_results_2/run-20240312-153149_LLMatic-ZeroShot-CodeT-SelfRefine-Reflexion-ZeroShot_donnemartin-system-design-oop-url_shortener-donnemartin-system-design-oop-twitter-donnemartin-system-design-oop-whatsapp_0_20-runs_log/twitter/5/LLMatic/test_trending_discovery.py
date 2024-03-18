import trending_discovery


def test_identify_trending_topics():
	trending_discovery.posts_db = {
		1: {'hashtags': ['#topic1', '#topic2']},
		2: {'hashtags': ['#topic2', '#topic3', '#topic1', '#topic1']},
		3: {'hashtags': ['#topic3', '#topic3']}
	}
	assert sorted(trending_discovery.identify_trending_topics()) == sorted([('#topic1', 3), ('#topic2', 2), ('#topic3', 3)])


def test_sort_trending_topics():
	trending_discovery.posts_db = {
		1: {'hashtags': ['#topic1', '#topic2']},
		2: {'hashtags': ['#topic2', '#topic3', '#topic1', '#topic1']},
		3: {'hashtags': ['#topic3', '#topic3']}
	}
	assert trending_discovery.sort_trending_topics() == [('#topic1', 3), ('#topic3', 3), ('#topic2', 2)]


def test_recommend_users_to_follow():
	trending_discovery.users_db = {
		1: {'following': [2, 3]},
		2: {'following': [3, 4]},
		3: {'following': [4, 5]},
		4: {'following': [5, 6]},
		5: {'following': [6, 7]},
		6: {'following': [7, 8]},
		7: {'following': [8, 9]},
		8: {'following': [9, 10]},
		9: {'following': [10, 1]},
		10: {'following': [1, 2]}
	}
	assert sorted(trending_discovery.recommend_users_to_follow(1)) == sorted([4, 5])
