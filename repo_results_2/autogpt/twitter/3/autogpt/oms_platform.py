class OMS:
    def __init__(self):
        self.users = []
        self.posts = []

    def get_trending_topics(self):
        topics = {}
        for post in self.posts:
            for word in post.content.split():
                if word not in topics:
                    topics[word] = 0
                topics[word] += 1
        return sorted(topics.items(), key=lambda x: x[1], reverse=True)[:10]

    def recommend_users(self, user):
        recommended = []
        for potential in self.users:
            if potential not in user.following and potential != user:
                recommended.append(potential)
        return recommended