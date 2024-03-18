import dataclasses

@dataclasses.dataclass
class TrendingDiscovery:
    trending_topics: dict
    user_recommendations: list

    def identify_trending_topics(self, posts):
        for post in posts:
            for word in post.content.split():
                if word not in self.trending_topics:
                    self.trending_topics[word] = 0
                self.trending_topics[word] += 1

    def display_trending_topics(self, location=None):
        if location:
            return sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)
        else:
            return sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)

    def recommend_users(self, user):
        for potential_user in User.users:
            if potential_user not in user.following and len(set(potential_user.followers) & set(user.followers)) > 0:
                self.user_recommendations.append(potential_user)