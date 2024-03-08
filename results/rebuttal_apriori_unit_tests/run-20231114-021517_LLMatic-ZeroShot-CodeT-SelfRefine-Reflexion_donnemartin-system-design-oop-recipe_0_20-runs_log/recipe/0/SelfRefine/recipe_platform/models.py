from dataclasses import dataclass
from typing import List, Dict

# Mock database
DATABASE = {
	'users': {},
	'recipes': {},
	'ratings': {},
	'reviews': {},
	'follows': {},
	'admins': {}
}

@dataclass
class User:
	id: int
	username: str
	password: str
	favorites: List[int]
	following: List[int]
	interests: List[str]

	def __init__(self, id: int, username: str, password: str, favorites: List[int] = None, following: List[int] = None, interests: List[str] = None):
		self.id = id
		self.username = username
		self.password = password
		self.favorites = favorites if favorites is not None else []
		self.following = following if following is not None else []
		self.interests = interests if interests is not None else []

	@staticmethod
	def create(id: int, username: str, password: str) -> 'User':
		user = User(id, username, password)
		DATABASE['users'][id] = user
		return user

	def change_password(self, new_password: str):
		self.password = new_password

	def save_favorite(self, recipe_id: int):
		self.favorites.append(recipe_id)

	def follow(self, user_id: int):
		self.following.append(user_id)

	def add_interest(self, interest: str):
		self.interests.append(interest)

	def get_notifications(self):
		# Mock implementation
		return ['new_{}_recipe'.format(interest) for interest in self.interests]

@dataclass
class Admin(User):
	def __init__(self, id: int, username: str, password: str, favorites: List[int] = None, following: List[int] = None, interests: List[str] = None):
		super().__init__(id, username, password, favorites, following, interests)

	@staticmethod
	def create(id: int, username: str, password: str) -> 'Admin':
		admin = Admin(id, username, password)
		DATABASE['admins'][id] = admin
		return admin

	def edit_recipe(self, recipe_id: int, new_data: Dict):
		recipe = DATABASE['recipes'].get(recipe_id)
		if recipe:
			recipe.__dict__.update(new_data)

	def remove_recipe(self, recipe_id: int):
		DATABASE['recipes'].pop(recipe_id, None)

	def get_site_statistics(self):
		# Mock implementation
		return {
			'total_users': len(DATABASE['users']),
			'total_recipes': len(DATABASE['recipes'])
		}

@dataclass
class Recipe:
	id: int
	title: str
	ingredients: List[str]
	instructions: str
	image: str
	categories: List[str]

	def __init__(self, id: int, title: str, ingredients: List[str], instructions: str, image: str, categories: List[str] = None):
		self.id = id
		self.title = title
		self.ingredients = ingredients
		self.instructions = instructions
		self.image = image
		self.categories = categories if categories is not None else []

	@staticmethod
	def create(id: int, title: str, ingredients: List[str], instructions: str, image: str, categories: List[str] = []) -> 'Recipe':
		recipe = Recipe(id, title, ingredients, instructions, image, categories)
		DATABASE['recipes'][id] = recipe
		return recipe

	def edit(self, new_data: Dict):
		self.__dict__.update(new_data)

	def delete(self):
		DATABASE['recipes'].pop(self.id, None)

	def is_valid(self):
		return bool(self.title and self.ingredients and self.instructions and self.image)

	def has_valid_categories(self):
		# Mock implementation
		return all(category in ['Italian', 'Vegan', 'Gluten-Free'] for category in self.categories)

@dataclass
class Rating:
	recipe_id: int
	rating: int

	@staticmethod
	def submit_rating(recipe_id: int, rating: int) -> 'Rating':
		rating_obj = Rating(recipe_id, rating)
		DATABASE['ratings'][recipe_id] = DATABASE['ratings'].get(recipe_id, []) + [rating_obj]
		return rating_obj

	@staticmethod
	def get_average_rating(recipe_id: int) -> float:
		ratings = [r.rating for r in DATABASE['ratings'].get(recipe_id, [])]
		return sum(ratings) / len(ratings) if ratings else 0

@dataclass
class Review:
	recipe_id: int
	text: str

	@staticmethod
	def submit_review(recipe_id: int, text: str) -> 'Review':
		review = Review(recipe_id, text)
		DATABASE['reviews'][recipe_id] = DATABASE['reviews'].get(recipe_id, []) + [review]
		return review

	@staticmethod
	def get_reviews(recipe_id: int) -> List['Review']:
		return DATABASE['reviews'].get(recipe_id, [])
