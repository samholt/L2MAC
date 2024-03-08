class ReviewManager:
    def __init__(self):
        self.reviews = []

    def rate_recipe(self, recipe_id, user_id, rating):
        # Add rating to reviews
        self.reviews.append({'recipe_id': recipe_id, 'user_id': user_id, 'rating': rating})
        return 'Rating submitted successfully'

    def write_review(self, recipe_id, user_id, review):
        # Add review to reviews
        self.reviews.append({'recipe_id': recipe_id, 'user_id': user_id, 'review': review})
        return 'Review submitted successfully'

    def display_average_rating(self, recipe_id):
        # Calculate and return average rating for a recipe
        ratings = [review['rating'] for review in self.reviews if review['recipe_id'] == recipe_id]
        return sum(ratings) / len(ratings) if ratings else 'No ratings yet'