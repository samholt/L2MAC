from flask import request, jsonify

reviews = []


def rate_recipe(recipe_id, rating):
    for review in reviews:
        if review['recipe_id'] == recipe_id:
            review['ratings'].append(rating)
            return jsonify({'message': 'Rating added successfully'}), 200
    reviews.append({'recipe_id': recipe_id, 'ratings': [rating]})
    return jsonify({'message': 'Rating added successfully'}), 200

def write_review(recipe_id, review):
    reviews.append({'recipe_id': recipe_id, 'review': review})
    return jsonify({'message': 'Review added successfully'}), 200

def display_average_rating(recipe_id):
    for review in reviews:
        if review['recipe_id'] == recipe_id:
            average_rating = sum(review['ratings']) / len(review['ratings'])
            return jsonify({'average_rating': average_rating}), 200
    return jsonify({'message': 'No ratings found'}), 404