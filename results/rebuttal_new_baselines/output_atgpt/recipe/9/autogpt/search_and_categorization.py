from flask import jsonify

recipes = []

def search_recipes(query):
    results = [recipe for recipe in recipes if query in recipe['name'] or query in recipe['ingredients'] or query in recipe['categories']]
    return jsonify(results), 200

def categorize_recipes(category):
    results = [recipe for recipe in recipes if category in recipe['categories']]
    return jsonify(results), 200