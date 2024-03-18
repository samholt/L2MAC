class SocialInteraction:
    def __init__(self):
        self.following = set()
        self.followers = set()
        self.direct_messages = []
        self.notifications = []

    def follow(self, user):
        self.following.add(user)
        user.followers.add(self)

    def unfollow(self, user):
        self.following.remove(user)
        user.followers.remove(self)

    def send_direct_message(self, user, message):
        self.direct_messages.append((user, message))
        user.notifications.append((self, message))

    def view_timeline(self):
        return sorted((post for user in self.following for post in user.posts), key=lambda post: post.timestamp, reverse=True)