class Rating:
    def __init__(self, user, recipe, rating):
        self.user = user
        self.recipe = recipe
        self.rating = rating

    def rate_recipe(self):
        # Code to rate recipe
        pass

class Review:
    def __init__(self, user, recipe, review):
        self.user = user
        self.recipe = recipe
        self.review = review

    def write_review(self):
        # Code to write review
        pass

class Community:
    def __init__(self, user):
        self.user = user

    def follow_user(self, user_to_follow):
        # Code to follow user
        pass

    def share_recipe(self, recipe):
        # Code to share recipe on social media
        pass