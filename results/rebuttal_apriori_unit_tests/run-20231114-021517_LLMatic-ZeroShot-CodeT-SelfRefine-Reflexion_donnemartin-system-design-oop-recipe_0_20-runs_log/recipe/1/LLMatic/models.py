class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.followed_users = []


class Recipe:
	def __init__(self, title, ingredients, instructions, image, categories):
		self.title = title
		self.ingredients = ingredients
		self.instructions = instructions
		self.image = image
		self.categories = categories
		self.ratings = []
		self.reviews = []

	def add_rating(self, rating):
		self.ratings.append(rating)

	def add_review(self, review):
		self.reviews.append(review)

	def get_average_rating(self):
		return sum(self.ratings) / len(self.ratings) if self.ratings else 0


class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.managed_recipes = []
		self.site_statistics = {}
