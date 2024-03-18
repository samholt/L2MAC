import collections

# Mock database
posts_db = {}
users_db = {}


def identify_trending_topics():
	# Identify trending topics based on the frequency of hashtags in posts
	all_hashtags = [hashtag for post in posts_db.values() for hashtag in post['hashtags']]
	counter = collections.Counter(all_hashtags)
	trending_topics = counter.most_common(10)
	return trending_topics


def display_trending_topics():
	# Display the top 10 trending topics
	trending_topics = identify_trending_topics()
	for topic in trending_topics:
		print(f'{topic[0]}: {topic[1]} times')


def sort_trending_topics():
	# Sort trending topics based on their frequency
	trending_topics = identify_trending_topics()
	trending_topics.sort(key=lambda x: x[1], reverse=True)
	return trending_topics


def recommend_users_to_follow(user_id):
	# Recommend users to follow based on the users that the given user's followings are following
	user_followings = users_db[user_id]['following']
	recommendations = [following for user in user_followings for following in users_db[user]['following'] if following not in user_followings and following != user_id]
	return list(set(recommendations))[:3]
