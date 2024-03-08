class UserRelationship:
    def __init__(self, follower, followed):
        self.follower = follower
        self.followed = followed


class PrivateMessage:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content


class Notification:
    def __init__(self, user, content):
        self.user = user
        self.content = content


def follow_user(follower, followed):
    relationship = UserRelationship(follower, followed)
    # TODO: Save relationship to database


def unfollow_user(follower, followed):
    # TODO: Remove relationship from database
    pass


def send_private_message(sender, receiver, content):
    message = PrivateMessage(sender, receiver, content)
    # TODO: Save message to database


def create_notification(user, content):
    notification = Notification(user, content)
    # TODO: Save notification to database
