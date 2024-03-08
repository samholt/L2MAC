class User:
    def __init__(self, username):
        self.username = username
        self.following = set()

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.discard(user)


class TwitterLikeSystem:
    def __init__(self):
        self.tweets = []
        self.direct_messages = []
        self.users = {}

    def register_user(self, username):
        user = User(username)
        self.users[username] = user
        return user

    def get_followed_users_tweets(self, user):
        followed_users_tweets = [tweet for tweet in self.tweets if tweet.user in user.following]
        return followed_users_tweets


if __name__ == '__main__':
    twitter_like_system = TwitterLikeSystem()
