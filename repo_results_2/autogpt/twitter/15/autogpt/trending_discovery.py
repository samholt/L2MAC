# Trending and discovery class
class TrendingDiscovery:
    def __init__(self):
        self.trending_topics = {}
        self.user_recommendations = {}

    # Update trending topics
    def update_trending_topics(self, topic):
        if topic not in self.trending_topics:
            self.trending_topics[topic] = 0
        self.trending_topics[topic] += 1

    # Get trending topics
    def get_trending_topics(self):
        return sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)

    # Update user recommendations
    def update_user_recommendations(self, user, recommendation):
        if user not in self.user_recommendations:
            self.user_recommendations[user] = []
        self.user_recommendations[user].append(recommendation)

    # Get user recommendations
    def get_user_recommendations(self, user):
        return self.user_recommendations[user] if user in self.user_recommendations else []