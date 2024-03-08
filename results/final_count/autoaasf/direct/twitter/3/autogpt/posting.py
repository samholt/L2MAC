from datetime import datetime


class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.likes = 0
        self.comments = []


def create_post(user, content):
    post = Post(user, content)
    # Save post to database (to be implemented)
    return post


def like_post(post):
    post.likes += 1
    # Update post in database (to be implemented)
    return post


def add_comment(post, user, comment):
    post.comments.append({'user': user, 'comment': comment})
    # Update post in database (to be implemented)
    return post


def search_posts(query):
    # Retrieve posts from database (to be implemented)
    posts = []
    filtered_posts = [post for post in posts if query.lower() in post.content.lower()]
    return filtered_posts
