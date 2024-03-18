class Post:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.interactions = {}

    def add_interaction(self, user, interaction):
        self.interactions[user] = interaction


class ContentManager:
    def __init__(self):
        self.posts = []

    def create_post(self, user, text):
        post = Post(user, text)
        self.posts.append(post)

    def search_posts(self, query):
        return [post for post in self.posts if query in post.text]

    def filter_posts(self, filter_func):
        return [post for post in self.posts if filter_func(post)]