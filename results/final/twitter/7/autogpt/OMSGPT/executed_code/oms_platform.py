class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.following = set()
        self.posts = []

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.discard(user)

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        return post


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = time.time()
        self.likes = set()

    def like(self, user):
        self.likes.add(user)

    def unlike(self, user):
        self.likes.discard(user)


class OMS:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, email):
        if username not in self.users:
            user = User(username, password, email)
            self.users[username] = user
            return user
        return None

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None

    def get_feed(self, user):
        feed = []
        for followed_user in user.following:
            feed.extend(followed_user.posts)
        feed.sort(key=lambda post: post.timestamp, reverse=True)
        return feed