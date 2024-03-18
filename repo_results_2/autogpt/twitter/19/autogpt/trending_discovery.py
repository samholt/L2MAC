import dataclasses
from collections import Counter

@dataclasses.dataclass
class TrendingDiscovery:
    user: User
    posts: list
    trending_topics: Counter
    recommended_users: list

    def identify_trending_topics(self):
        for post in self.posts:
            for word in post.content.split():
                self.trending_topics[word] += 1

    def display_trending_topics(self, location=None):
        if location:
            return sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)
        else:
            return sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)

    def recommend_users(self):
        for user in self.user.following:
            if user not in self.recommended_users and user.followers > 1000:
                self.recommended_users.append(user)