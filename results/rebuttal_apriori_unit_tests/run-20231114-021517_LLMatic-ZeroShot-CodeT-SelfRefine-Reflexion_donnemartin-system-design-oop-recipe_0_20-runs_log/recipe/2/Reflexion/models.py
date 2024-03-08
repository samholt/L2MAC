from dataclasses import dataclass

@dataclass
class User:
	id: int
	username: str
	password: str
	recipes: list
	favorites: list
	follows: list

@dataclass
class Recipe:
	id: int
	name: str
	ingredients: list
	instructions: str
	image: str
	categories: list
	reviews: list

@dataclass
class Review:
	id: int
	user_id: int
	recipe_id: int
	rating: int
	comment: str
