class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content

class PostManager:
    def create_post(self, user, content):
        return Post(user, content)
    def interact_with_post(self, post):
        # This is a placeholder. In a real system, we would implement likes, comments, etc.
        return 'User interacted with post'