import time


class Post:
    def __init__(self, user, content, image=None):
        self.user = user
        self.content = content
        self.image = image
        self.timestamp = time.time()
        self.likes = 0
        self.retweets = 0
        self.replies = []

    def like(self):
        self.likes += 1

    def retweet(self):
        self.retweets += 1

    def reply(self, reply_post):
        self.replies.append(reply_post)


def create_post(user, content, image=None):
    if len(content) > 280:
        raise ValueError('Content exceeds the 280 character limit.')
    post = Post(user, content, image)
    # TODO: Save post to database
    return post


def delete_post(post):
    # TODO: Delete post from database
    pass


def like_post(post):
    post.like()
    # TODO: Update post in database


def retweet_post(post):
    post.retweet()
    # TODO: Update post in database


def reply_to_post(post, reply_content, reply_image=None):
    reply_post = create_post(post.user, reply_content, reply_image)
    post.reply(reply_post)
    # TODO: Update post in database
