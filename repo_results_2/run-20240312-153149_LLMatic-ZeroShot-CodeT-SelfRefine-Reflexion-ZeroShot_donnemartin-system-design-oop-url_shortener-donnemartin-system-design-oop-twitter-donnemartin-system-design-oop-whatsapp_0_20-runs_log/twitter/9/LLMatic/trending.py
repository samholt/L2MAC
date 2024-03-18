import random

# Mock database
posts_db = {}


def get_trending_topics():
	# For simplicity, we will randomly generate trending topics
	topics = ['topic' + str(i) for i in range(10)]
	return random.sample(topics, 5)


def sort_trending_topics(location):
	# For simplicity, we will randomly generate trending topics
	topics = ['topic' + str(i) for i in range(10)]
	# Sort based on location
	topics.sort(key=lambda x: hash(x + location))
	return topics
