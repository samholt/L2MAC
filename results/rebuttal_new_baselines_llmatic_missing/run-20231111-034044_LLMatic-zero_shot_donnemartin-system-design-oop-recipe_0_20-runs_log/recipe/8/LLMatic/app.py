from flask import Flask, request, jsonify
import users
import recipes
import reviews
import categories
import admin
import recommendations

app = Flask(__name__)

user_manager = users.UserManager()
recipe_manager = recipes.Recipe()
review_manager = reviews
category_manager = categories.Categories()
admin_manager = admin.Admin()
recommendation_manager = recommendations.Recommendations(user_manager, recipe_manager)

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
	if request.method == 'POST':
		data = request.get_json()
		return jsonify(user_manager.create_user(data['username'], data['password']))
	else:
		return jsonify({user.username: user.__dict__ for user in user_manager.users.values()})

@app.route('/recipes', methods=['GET', 'POST'])
def handle_recipes():
	if request.method == 'POST':
		data = request.get_json()
		recipe_manager.submit_recipe(data['recipe_id'], data)
		return jsonify({'message': 'Recipe submitted successfully'})
	else:
		return jsonify(recipe_manager.recipes)

@app.route('/reviews', methods=['GET', 'POST'])
def handle_reviews():
	if request.method == 'POST':
		data = request.get_json()
		review = review_manager.submit_review(data['username'], data['recipe'], data['rating'], data['review_text'])
		return jsonify({'message': 'Review submitted successfully', 'review': review.__dict__})
	else:
		return jsonify({username: review.__dict__ for username, review in review_manager.mock_db.items()})

@app.route('/categories', methods=['GET', 'POST'])
def handle_categories():
	if request.method == 'POST':
		data = request.get_json()
		category_manager.recipes[data['recipe_id']] = data
		return jsonify({'message': 'Recipe categorized successfully'})
	else:
		return jsonify(category_manager.recipes)

@app.route('/admin', methods=['GET', 'POST'])
def handle_admin():
	if request.method == 'POST':
		data = request.get_json()
		return jsonify({'message': admin_manager.manage_recipes(data['recipe_id'], data['action'])})
	else:
		return jsonify(admin_manager.database)

@app.route('/recommendations', methods=['GET', 'POST'])
def handle_recommendations():
	if request.method == 'POST':
		data = request.get_json()
		return jsonify({'message': 'Recommendations generated successfully', 'recommendations': recommendation_manager.generate_recommendations(data['username'])})
	else:
		return jsonify({user.username: user.__dict__ for user in user_manager.users.values()})

if __name__ == '__main__':
	app.run(debug=True)
