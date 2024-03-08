from flask import Flask, request, jsonify
from user import User
from recipe import Recipe
from review import Review
from search import Search
from admin import Admin
from feed import Feed
from recommendation import Recommendation

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User.register(data)
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.login(data)
	return jsonify(user.to_dict()), 200

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe.create(data)
	return jsonify(recipe.to_dict()), 201

@app.route('/recipe/<int:recipe_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_recipe(recipe_id):
	if request.method == 'GET':
		recipe = Recipe.get(recipe_id)
		return jsonify(recipe.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		recipe = Recipe.update(recipe_id, data)
		return jsonify(recipe.to_dict()), 200
	elif request.method == 'DELETE':
		Recipe.delete(recipe_id)
		return '', 204

@app.route('/review', methods=['POST'])
def post_review():
	data = request.get_json()
	review = Review.post(data)
	return jsonify(review.to_dict()), 201

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('query')
	results = Search.query(query)
	return jsonify(results), 200

@app.route('/admin', methods=['POST'])
def admin_action():
	data = request.get_json()
	Admin.perform_action(data)
	return '', 204

@app.route('/feed', methods=['GET'])
def view_feed():
	feed = Feed.view()
	return jsonify(feed), 200

@app.route('/recommendation', methods=['GET'])
def get_recommendation():
	recommendation = Recommendation.generate()
	return jsonify(recommendation), 200

if __name__ == '__main__':
	app.run(debug=True)
