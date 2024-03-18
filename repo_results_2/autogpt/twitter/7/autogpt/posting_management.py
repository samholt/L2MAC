from datetime import datetime


class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.created_at = datetime.now()
        self.likes = 0
        self.comments = []

    def like(self):
        self.likes += 1

    def comment(self, user, content):
        self.comments.append({'user': user, 'content': content, 'created_at': datetime.now()})