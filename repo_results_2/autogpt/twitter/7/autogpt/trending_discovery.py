from collections import Counter


class TrendingDiscovery:
    def __init__(self):
        self.topics = Counter()

    def add_topic(self, topic):
        self.topics[topic] += 1

    def get_trending_topics(self):
        return self.topics.most_common(10)

    def recommend_users(self, user):
        # This is a simple recommendation algorithm that recommends the users that the user's following are following
        recommended_users = set()
        for following in user.following:
            recommended_users.update(following.following)
        recommended_users.difference_update(user.following)
        return recommended_users