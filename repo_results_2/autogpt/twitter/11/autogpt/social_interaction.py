import dataclasses

@dataclasses.dataclass
class SocialInteraction:
    user: User
    followers: list
    following: list
    timeline: list
    messages: dict
    notifications: list

    def follow_user(self, user_to_follow):
        self.following.append(user_to_follow)
        user_to_follow.followers.append(self)

    def unfollow_user(self, user_to_unfollow):
        self.following.remove(user_to_unfollow)
        user_to_unfollow.followers.remove(self)

    def view_timeline(self):
        return self.timeline

    def send_message(self, recipient, message):
        self.messages[recipient] = message

    def receive_notification(self, notification):
        self.notifications.append(notification)