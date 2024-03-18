# Social interaction class
class SocialInteraction:
    def __init__(self):
        self.following = {}
        self.messages = {}

    # Follow a user
    def follow(self, user):
        self.following[user] = True

    # Unfollow a user
    def unfollow(self, user):
        if user in self.following:
            del self.following[user]

    # Send a message to a user
    def send_message(self, user, message):
        if user not in self.messages:
            self.messages[user] = []
        self.messages[user].append(message)

    # Get the timeline of a user
    def get_timeline(self, user):
        return self.messages[user] if user in self.messages else []