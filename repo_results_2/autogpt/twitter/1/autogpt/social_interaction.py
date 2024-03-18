class SocialInteraction:
    def __init__(self):
        self.following = set()
        self.direct_messages = {}
        self.notifications = []

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.discard(user)

    def send_direct_message(self, recipient, message):
        if recipient not in self.direct_messages:
            self.direct_messages[recipient] = []
        self.direct_messages[recipient].append(message)

    def add_notification(self, notification):
        self.notifications.append(notification)

    def view_timeline(self):
        return [post for user in self.following for post in user.posts]