

class User:
    def __init__(self, username):
        self.username = username
        self.following = set()
        self.messages = {}
        self.notifications = []

    def follow(self, other_user):
        self.following.add(other_user.username)
        self.notifications.append(f'You are now following {other_user.username}')

    def unfollow(self, other_user):
        self.following.discard(other_user.username)
        self.notifications.append(f'You have unfollowed {other_user.username}')

    def view_timeline(self, post_db):
        timeline_posts = [post for post in post_db.posts.values() if post.user.username in self.following]
        timeline_posts.sort(key=lambda post: post.created_at, reverse=True)
        return timeline_posts

    def send_message(self, other_user, message):
        if other_user.username not in self.messages:
            self.messages[other_user.username] = []
        self.messages[other_user.username].append(message)
        self.notifications.append(f'You have a new message from {other_user.username}')

    def view_notifications(self):
        return self.notifications