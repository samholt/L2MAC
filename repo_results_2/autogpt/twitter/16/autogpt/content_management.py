class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.likes = 0
        self.comments = []

    def like(self):
        self.likes += 1

    def comment(self, user, comment):
        self.comments.append((user, comment))


class PostManager:
    def __init__(self):
        self.posts = []

    def create_post(self, user, content):
        post = Post(user, content)
        self.posts.append(post)
        return 'Post created successfully'

    def like_post(self, post_id):
        if post_id >= len(self.posts):
            return 'Post does not exist'
        self.posts[post_id].like()
        return 'Post liked successfully'

    def comment_on_post(self, post_id, user, comment):
        if post_id >= len(self.posts):
            return 'Post does not exist'
        self.posts[post_id].comment(user, comment)
        return 'Comment added successfully'