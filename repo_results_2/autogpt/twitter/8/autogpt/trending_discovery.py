from collections import Counter

# TrendingDiscovery class
class TrendingDiscovery:
    def __init__(self, posts):
        self.posts = posts

    # Method to get trending topics
    def get_trending_topics(self):
        topics = [post.content for post in self.posts]
        return Counter(topics).most_common(10)

    # Method to get user recommendations
    def get_user_recommendations(self, user):
        following = user.following
        recommendations = [post.user for post in self.posts if post.user not in following]
        return Counter(recommendations).most_common(10)