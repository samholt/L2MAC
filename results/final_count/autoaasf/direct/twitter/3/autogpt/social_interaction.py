class UserProfile:
    def __init__(self, user):
        self.user = user
        self.following = set()
        self.messages = []
        self.notifications = []


def follow(user_profile, target_profile):
    user_profile.following.add(target_profile.user)
    # Update user profile in database (to be implemented)
    add_notification(target_profile, f'{user_profile.user.username} started following you.')


def unfollow(user_profile, target_profile):
    user_profile.following.discard(target_profile.user)
    # Update user profile in database (to be implemented)


def send_message(sender_profile, recipient_profile, message):
    message_data = {'sender': sender_profile.user, 'recipient': recipient_profile.user, 'message': message}
    sender_profile.messages.append(message_data)
    recipient_profile.messages.append(message_data)
    # Update sender and recipient profiles in database (to be implemented)
    add_notification(recipient_profile, f'New message from {sender_profile.user.username}.')


def add_notification(user_profile, message):
    user_profile.notifications.append({'message': message, 'read': False})
    # Update user profile in database (to be implemented)


def mark_notification_as_read(user_profile, notification_index):
    user_profile.notifications[notification_index]['read'] = True
    # Update user profile in database (to be implemented)
