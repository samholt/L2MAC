class SocialInteraction:
    def __init__(self, user):
        self.user = user
        self.following = set()
        self.messages = []
        self.notifications = []

    def follow(self, other_user):
        self.following.add(other_user)
        other_user.notifications.append(f'{self.user.username} started following you')

    def send_message(self, other_user, message):
        other_user.messages.append((self.user, message))
        other_user.notifications.append(f'You have a new message from {self.user.username}')


class SocialInteractionManager:
    def __init__(self):
        self.interactions = {}

    def create_interaction(self, user):
        self.interactions[user.username] = SocialInteraction(user)

    def follow(self, username, other_username):
        if username not in self.interactions or other_username not in self.interactions:
            return 'User does not exist'
        self.interactions[username].follow(self.interactions[other_username])
        return 'Followed successfully'

    def send_message(self, username, other_username, message):
        if username not in self.interactions or other_username not in self.interactions:
            return 'User does not exist'
        self.interactions[username].send_message(self.interactions[other_username], message)
        return 'Message sent successfully'