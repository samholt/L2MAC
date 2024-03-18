class Recommendation:
	def __init__(self, user_class):
		self.user_class = user_class

	def get_recommendations(self, user):
		if user not in self.user_class.users:
			return 'User not found'
		recommendations_based_on_followers = []
		recommendations_based_on_following = []
		for other_user in self.user_class.users:
			if other_user != user and other_user not in self.user_class.users[user]['following']:
				mutual_followers = len(set(self.user_class.users[user]['followers']).intersection(set(self.user_class.users[other_user]['followers'])))
				if mutual_followers > 0:
					recommendations_based_on_followers.append((other_user, mutual_followers))
			for following_user in self.user_class.users[user]['following']:
				for followed_by_following in self.user_class.users[following_user]['following']:
					if followed_by_following != user and followed_by_following not in self.user_class.users[user]['following'] and followed_by_following not in [user for user, _ in recommendations_based_on_followers]:
						recommendations_based_on_following.append(followed_by_following)
			for follower_user in self.user_class.users[user]['followers']:
				for followed_by_follower in self.user_class.users[follower_user]['following']:
					if followed_by_follower != user and followed_by_follower not in self.user_class.users[user]['following'] and followed_by_follower not in [user for user, _ in recommendations_based_on_followers] and followed_by_follower not in recommendations_based_on_following:
						recommendations_based_on_following.append(followed_by_follower)
		recommendations_based_on_followers.sort(key=lambda x: x[1], reverse=True)
		recommendations_based_on_following = list(set(recommendations_based_on_following))
		recommendations_based_on_following.sort()
		return list(set([user for user, mutual_followers in recommendations_based_on_followers] + recommendations_based_on_following))
