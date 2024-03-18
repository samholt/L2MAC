from collections import Counter


class Trending:
    def __init__(self, posts):
        self.posts = posts

    def get_trending_topics(self):
        topics = Counter()
        for post in self.posts:
            topics.update(post.content.split())
        return topics.most_common(10)


class Discovery:
    def __init__(self, users):
        self.users = users

    def recommend_users(self, user):
        return [other for other in self.users if other not in user.following and other.followers & user.following]