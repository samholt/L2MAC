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
        self.timestamp = datetime.datetime.now()


class OMS:
    def __init__(self):
        self.users = {}
        self.posts = []

    def register_user(self, username, password, email):
        if username not in self.users:
            user = User(username, password, email)
            self.users[username] = user
            return user
        return None

    def create_post(self, username, content):
        user = self.users.get(username)
        if user:
            post = user.create_post(content)
            self.posts.append(post)
            return post
        return None

    def get_timeline(self, username):
        user = self.users.get(username)
        if user:
            timeline = [post for post in self.posts if post.author in user.following]
            return timeline
        return None