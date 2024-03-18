class SocialInteraction:
    def __init__(self, user):
        self.user = user
        self.following = set()
        self.followers = set()
        self.messages = []
        self.notifications = []

    def follow(self, other_user):
        self.following.add(other_user)
        other_user.followers.add(self.user)

    def unfollow(self, other_user):
        self.following.remove(other_user)
        other_user.followers.remove(self.user)

    def send_message(self, other_user, message):
        self.messages.append({'to': other_user, 'message': message})
        other_user.notifications.append({'from': self.user, 'message': message})