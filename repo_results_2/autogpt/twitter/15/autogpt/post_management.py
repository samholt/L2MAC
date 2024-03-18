# Post class
class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.interactions = {}

    # Add interaction to post
    def add_interaction(self, user, interaction):
        self.interactions[user] = interaction

# Post management class
class PostManagement:
    def __init__(self):
        self.posts = []

    # Create new post
    def create_post(self, user, content):
        post = Post(user, content)
        self.posts.append(post)
        return post

    # Add interaction to post
    def add_interaction(self, post, user, interaction):
        post.add_interaction(user, interaction)

    # Filter posts by user
    def filter_by_user(self, user):
        return [post for post in self.posts if post.user == user]

    # Search posts by content
    def search_posts(self, query):
        return [post for post in self.posts if query in post.content]