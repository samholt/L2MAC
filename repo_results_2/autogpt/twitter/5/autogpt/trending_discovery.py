# Trending & Discovery Code

# Trending Topics
class Topic:
    def __init__(self, name):
        self.name = name
        self.mentions = 0

topics = []

def mention_topic(post, topic):
    if topic not in topics:
        new_topic = Topic(topic)
        topics.append(new_topic)
    else:
        topic.mentions += 1
    post.text += f' #{topic}'
    return 'Topic mentioned'

def get_trending_topics():
    return sorted(topics, key=lambda topic: topic.mentions, reverse=True)

# User Recommendations
def recommend_users(user):
    recommended_users = []
    for other_user in users:
        if other_user != user and len(set(user.following) & set(other_user.following)) > 0:
            recommended_users.append(other_user)
    return recommended_users