from collections import Counter


class TrendingDiscovery:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_trending_topics(self):
        topics = [topic for post in self.posts for topic in post.text.split() if topic.startswith('#')]
        return Counter(topics).most_common()

    def get_user_recommendations(self, user):
        followed_users = set(user.following)
        recommended_users = [post.user for post in self.posts if post.user not in followed_users]
        return Counter(recommended_users).most_common()