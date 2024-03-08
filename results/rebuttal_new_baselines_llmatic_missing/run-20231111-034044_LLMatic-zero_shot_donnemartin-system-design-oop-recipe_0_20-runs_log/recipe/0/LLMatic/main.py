from flask import Flask, request
from user import User
from recipe import Recipe
from review import Review
from search import Search
from admin import Admin
from feed import Feed
from recommendation import Recommendation

app = Flask(__name__)

# Mock database
users = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	user = User(data['username'], data['password'])
	users[data['username']] = user
	return 'Account created', 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	recipe = Recipe.create_recipe(data['id'], data['recipe'], data['category'], data['ingredients'], data['instructions'])
	return 'Recipe submitted', 200

@app.route('/submit_review', methods=['POST'])
def submit_review():
	data = request.get_json()
	review = Review.create_review(data['id'], data['user'], data['rating'], data['content'])
	return 'Review submitted', 200

@app.route('/search', methods=['GET'])
def search():
	data = request.args
	search = Search()
	results = search.search_by_name(data['query'])
	return {'results': results}, 200

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	data = request.get_json()
	admin = Admin(data['action'], data['target'])
	admin.remove_recipe(data['target'])
	return 'Admin action performed', 200

@app.route('/feed', methods=['GET'])
def feed():
	data = request.args
	feed = Feed(users[data['user_id']])
	feed_items = feed.generate_feed()
	return {'feed': feed_items}, 200

@app.route('/recommendation', methods=['GET'])
def recommendation():
	data = request.args
	recommendation = Recommendation(users, Recipe.get_all_recipes())
	recommendations = recommendation.generate_recommendations(data['user_id'])
	return {'recommendations': recommendations}, 200

if __name__ == '__main__':
	app.run(debug=True)
