from flask import Flask, request, jsonify
from user import User
from recipe import Recipe
from search import Search
from rating import Rating
from review import Review
from follow import Follow
from feed import Feed
from admin import Admin
from recommendation import Recommendation

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['username'], data['password'], data['email'])
	users[user.username] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(data['name'], data['ingredients'], data['instructions'], data['images'], data['categories'])
	recipes[recipe.name] = recipe
	return jsonify({'message': 'Recipe created successfully'}), 201

@app.route('/search', methods=['GET'])
def search():
	search = Search(recipes)
	results = search.search_by_name(request.args.get('name'))
	return jsonify({'results': [recipe.name for recipe in results]}), 200

@app.route('/rate', methods=['POST'])
def rate():
	data = request.get_json()
	rating = Rating(data['user_id'], data['recipe_id'], data['rating'])
	rating.rate_recipe()
	return jsonify({'message': 'Recipe rated successfully'}), 200

@app.route('/review', methods=['POST'])
def review():
	data = request.get_json()
	review = Review(data['user_id'], data['recipe_id'], data['review'])
	review.write_review()
	return jsonify({'message': 'Review written successfully'}), 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	follow = Follow()
	follow.follow(data['follower_id'], data['followee_id'])
	return jsonify({'message': 'User followed successfully'}), 200

@app.route('/feed', methods=['GET'])
def feed():
	feed = Feed()
	follow = Follow()
	activities = feed.get_feed(request.args.get('user_id'), follow)
	return jsonify({'feed': activities}), 200

@app.route('/admin', methods=['GET'])
def admin():
	admin = Admin()
	statistics = admin.get_site_statistics()
	return jsonify(statistics), 200

@app.route('/recommend', methods=['GET'])
def recommend():
	recommendation = Recommendation()
	recommendations = recommendation.generate_recommendations(request.args.get('user_id'))
	return jsonify({'recommendations': recommendations}), 200

if __name__ == '__main__':
	app.run(debug=True)
