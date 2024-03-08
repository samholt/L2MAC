class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.posts = []

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
        else:
            return None

    def create_post(self, username, content):
        user = self.users.get(username)
        if user:
            post = user.create_post(content)
            self.posts.append(post)
            return post
        else:
            return None

    def get_posts(self):
        return self.posts

    def get_user_posts(self, username):
        user = self.users.get(username)
        if user:
            return user.posts
        else:
            return None