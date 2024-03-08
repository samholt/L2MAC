class Recommendations:
	def __init__(self, user_manager, recipe_manager):
		self.user_manager = user_manager
		self.recipe_manager = recipe_manager

	def generate_recommendations(self, username):
		user = self.user_manager.get_user(username)
		if user == 'User not found':
			return user
		# For simplicity, we will recommend the recipes submitted by the users that the current user follows
		recommended_recipes = []
		for followed_user in user.followed_users:
			recommended_recipes.extend(followed_user.submitted_recipes)
		return recommended_recipes

	def send_notifications(self, username, new_recipes):
		user = self.user_manager.get_user(username)
		if user == 'User not found':
			return user
		# For simplicity, we will notify the user about the new recipes submitted by the users that they follow
		notifications = []
		for followed_user in user.followed_users:
			for recipe in new_recipes:
				if recipe in followed_user.submitted_recipes:
					notifications.append(f'New recipe {recipe} from {followed_user.username}')
		return notifications
