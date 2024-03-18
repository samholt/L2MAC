# Social Interaction Code

# Following & Followers
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.following = []
        self.followers = []
        self.messages = []
        self.notifications = []

def follow(user, other_user):
    if other_user not in user.following:
        user.following.append(other_user)
        other_user.followers.append(user)
        other_user.notifications.append(f'{user.username} followed you')
        return 'User followed'
    return 'User already followed'

def unfollow(user, other_user):
    if other_user in user.following:
        user.following.remove(other_user)
        other_user.followers.remove(user)
        return 'User unfollowed'
    return 'User not followed'

# Direct Messaging
class Message:
    def __init__(self, sender, receiver, text):
        self.sender = sender
        self.receiver = receiver
        self.text = text

def send_message(sender, receiver, text):
    new_message = Message(sender, receiver, text)
    sender.messages.append(new_message)
    receiver.messages.append(new_message)
    receiver.notifications.append(f'New message from {sender.username}')
    return 'Message sent'

# Notifications
def check_notifications(user):
    return user.notifications