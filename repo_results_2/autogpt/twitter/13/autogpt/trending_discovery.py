class TrendingDiscovery:
    def __init__(self):
        self.trending_topics = []
        self.user_recommendations = []

class TrendingDiscoveryManager:
    def update_trending_topics(self, topics):
        self.trending_topics = topics
        return self
    def update_user_recommendations(self, users):
        self.user_recommendations = users
        return self