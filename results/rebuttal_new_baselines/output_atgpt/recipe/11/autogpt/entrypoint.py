# Import necessary modules
import os
import sys
from flask import Flask, request, jsonify
from recipe_manager import RecipeManager
from user_manager import UserManager
from search_manager import SearchManager
from review_manager import ReviewManager

# Initialize Flask app
app = Flask(__name__)

# Initialize managers
recipe_manager = RecipeManager()
user_manager = UserManager()
search_manager = SearchManager()
review_manager = ReviewManager()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)