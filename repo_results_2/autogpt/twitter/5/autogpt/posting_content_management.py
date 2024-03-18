# Posting and Content Management Code

# Creating Posts
class Post:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.likes = 0
        self.comments = []

posts = []

def create_post(user, text):
    new_post = Post(user, text)
    posts.append(new_post)
    return 'Post created successfully'

# Interacting with Posts
def like_post(post):
    post.likes += 1
    return 'Post liked'

def comment_post(post, user, comment):
    post.comments.append((user, comment))
    return 'Comment added'

# Content Filtering & Search
def search_posts(text):
    return [post for post in posts if text in post.text]

def filter_posts(user):
    return [post for post in posts if post.user == user]