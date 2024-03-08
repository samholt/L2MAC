class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.interactions = []

# Creating posts
def create_post(user, content):
    return Post(user, content)

# Interacting with posts
def interact_with_post(user, post, interaction):
    post.interactions.append((user, interaction))

# Content filtering & search
def filter_posts(posts, filter):
    # TODO: Add code to filter posts
    return [post for post in posts if filter(post)]