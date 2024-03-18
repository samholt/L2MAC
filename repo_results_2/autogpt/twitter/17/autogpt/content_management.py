class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.interactions = []

    def add_interaction(self, interaction):
        self.interactions.append(interaction)


class Interaction:
    def __init__(self, user, type):
        self.user = user
        self.type = type


class ContentFilter:
    def __init__(self, keywords):
        self.keywords = keywords

    def filter(self, posts):
        return [post for post in posts if any(keyword in post.content for keyword in self.keywords)]


class ContentSearch:
    def __init__(self, query):
        self.query = query

    def search(self, posts):
        return [post for post in posts if self.query in post.content]