from models import User, Recipe, Admin

# Mock database
users_db = {}
recipes_db = {}


def create_user(username, password, is_admin=False):
	if is_admin:
		user = Admin(username, password)
	else:
		user = User(username, password)
	users_db[username] = user
	return user


def change_password(username, new_password):
	user = users_db.get(username)
	if user:
		user.password = new_password


def save_favorite(username, recipe_title):
	user = users_db.get(username)
	recipe = recipes_db.get(recipe_title)
	if user and recipe and recipe not in user.favorite_recipes:
		user.favorite_recipes.append(recipe)


def get_profile(username):
	return users_db.get(username)


def submit_recipe(user, title, ingredients, instructions, image, categories):
	recipe = Recipe(title, ingredients, instructions, image, categories)
	user.submitted_recipes.append(recipe)
	recipes_db[recipe.title] = recipe
	return recipe


def edit_recipe(user, recipe_title, new_data):
	recipe = [r for r in user.submitted_recipes if r.title == recipe_title][0]
	if recipe:
		for key, value in new_data.items():
			setattr(recipe, key, value)
			if key == 'title':
				recipes_db[value] = recipe
				if value != recipe_title:
					del recipes_db[recipe_title]


def delete_recipe(user, recipe_title):
	recipe = [r for r in user.submitted_recipes if r.title == recipe_title][0]
	if recipe:
		user.submitted_recipes.remove(recipe)
		del recipes_db[recipe.title]


def search_recipes(query):
	return [recipe for recipe in recipes_db.values() if query in recipe.title or query in recipe.ingredients or query in recipe.categories]


def categorize_recipes(category):
	return [recipe for recipe in recipes_db.values() if category in recipe.categories]


def rate_recipe(username, recipe_title, rating):
	user = users_db.get(username)
	recipe = recipes_db.get(recipe_title)
	if user and recipe:
		recipe.add_rating(rating)


def write_review(username, recipe_title, review):
	user = users_db.get(username)
	recipe = recipes_db.get(recipe_title)
	if user and recipe:
		recipe.add_review(review)


def get_average_rating(recipe_title):
	recipe = recipes_db.get(recipe_title)
	if recipe:
		return recipe.get_average_rating()


def follow_user(follower_username, followee_username):
	follower = users_db.get(follower_username)
	followee = users_db.get(followee_username)
	if follower and followee and followee not in follower.followed_users:
		follower.followed_users.append(followee)


def get_feed(username):
	user = users_db.get(username)
	if user:
		feed = {'recent_activity': []}
		for followed_user in user.followed_users:
			for recipe in followed_user.submitted_recipes:
				feed['recent_activity'].append({'type': 'new_recipe', 'recipe': recipe.title, 'user': followed_user.username})
			for recipe in recipes_db.values():
				if recipe.ratings:
					feed['recent_activity'].append({'type': 'new_rating', 'recipe': recipe.title, 'rating': recipe.get_average_rating()})
		return feed


def share_recipe(username, recipe_title, platform):
	user = users_db.get(username)
	recipe = recipes_db.get(recipe_title)
	if user and recipe:
		# Mock sharing on social media
		return True
	return False


def manage_recipe(admin_username, recipe_title, new_data):
	admin = users_db.get(admin_username)
	recipe = recipes_db.get(recipe_title)
	if isinstance(admin, Admin) and recipe:
		for key, value in new_data.items():
			setattr(recipe, key, value)
			if key == 'title':
				recipes_db[value] = recipe
				if value != recipe_title:
					del recipes_db[recipe_title]


def remove_recipe(admin_username, recipe_title):
	admin = users_db.get(admin_username)
	recipe = recipes_db.get(recipe_title)
	if isinstance(admin, Admin) and recipe:
		del recipes_db[recipe_title]


def get_site_statistics(admin_username):
	admin = users_db.get(admin_username)
	if isinstance(admin, Admin):
		admin.site_statistics = {
			'total_users': len(users_db),
			'total_recipes': len(recipes_db)
		}
		return admin.site_statistics
