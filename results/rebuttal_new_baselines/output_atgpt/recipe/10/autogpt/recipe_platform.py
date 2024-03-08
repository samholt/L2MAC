# Recipe Sharing Platform

# Classes

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.recipes = []

    def register(self):
        pass

    def login(self):
        pass

    def submit_recipe(self, recipe):
        self.recipes.append(recipe)

class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.ratings = []
        self.reviews = []

    def rate(self, rating):
        self.ratings.append(rating)

    def review(self, review):
        self.reviews.append(review)

class Platform:
    def __init__(self):
        self.users = []
        self.recipes = []

    def register_user(self, user):
        self.users.append(user)

    def login_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def submit_recipe(self, recipe):
        self.recipes.append(recipe)

    def discover_recipe(self):
        return self.recipes