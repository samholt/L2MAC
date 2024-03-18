from collections import Counter


class TrendingDiscovery:
    def __init__(self, post_manager):
        self.post_manager = post_manager

    def get_trending_topics(self):
        topics = [post.content for post in self.post_manager.posts]
        counter = Counter(topics)
        return counter.most_common(10)

    def get_user_recommendations(self, user):
        following = user.following
        recommendations = [post.user for post in self.post_manager.posts if post.user not in following]
        counter = Counter(recommendations)
        return counter.most_common(10)