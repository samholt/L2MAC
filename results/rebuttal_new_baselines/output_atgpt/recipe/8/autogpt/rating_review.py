class Rating:
    def __init__(self, user, recipe, rating):
        self.user = user
        self.recipe = recipe
        self.rating = rating

    def rate_recipe(self):
        pass

class Review:
    def __init__(self, user, recipe, review):
        self.user = user
        self.recipe = recipe
        self.review = review

    def write_review(self):
        pass