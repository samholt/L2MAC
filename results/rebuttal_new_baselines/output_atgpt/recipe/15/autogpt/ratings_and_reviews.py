class RatingsAndReviews:
    def __init__(self):
        self.ratings = []
        self.reviews = []

    def rate_recipe(self, recipe_id, user, rating):
        # Add the rating to the list of ratings
        self.ratings.append({'recipe_id': recipe_id, 'user': user, 'rating': rating})

    def write_review(self, recipe_id, user, review):
        # Add the review to the list of reviews
        self.reviews.append({'recipe_id': recipe_id, 'user': user, 'review': review})

    def display_average_rating(self, recipe_id):
        # Calculate and display the average rating for the recipe
        recipe_ratings = [rating['rating'] for rating in self.ratings if rating['recipe_id'] == recipe_id]
        if recipe_ratings:
            average_rating = sum(recipe_ratings) / len(recipe_ratings)
            return average_rating
        return None