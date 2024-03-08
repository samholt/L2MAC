# Import necessary modules
from flask import request, jsonify

# List to store ratings and reviews
ratings_and_reviews = []

# Function to rate a recipe
def rate_recipe(recipe_id, rating):
    # Add rating to list
    ratings_and_reviews.append({'recipe_id': recipe_id, 'rating': rating})
    return jsonify({'message': 'Rating submitted successfully'}), 200

# Function to write a review
def write_review(recipe_id, review):
    # Add review to list
    ratings_and_reviews.append({'recipe_id': recipe_id, 'review': review})
    return jsonify({'message': 'Review submitted successfully'}), 200

# Function to display average rating on recipe page
def display_average_rating(recipe_id):
    # Calculate and return average rating
    ratings = [r['rating'] for r in ratings_and_reviews if r['recipe_id'] == recipe_id]
    if ratings:
        average_rating = sum(ratings) / len(ratings)
        return jsonify({'average_rating': average_rating}), 200
    return jsonify({'message': 'No ratings found'}), 404