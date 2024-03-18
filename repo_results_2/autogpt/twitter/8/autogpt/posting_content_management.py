from datetime import datetime

# Post class
class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.interactions = {}

    # Method to add interaction
    def add_interaction(self, user, interaction):
        self.interactions[user] = interaction

# ContentManager class
class ContentManager:
    def __init__(self):
        self.posts = []

    # Method to create post
    def create_post(self, user, content):
        post = Post(user, content)
        self.posts.append(post)

    # Method to search posts
    def search_posts(self, query):
        return [post for post in self.posts if query in post.content]