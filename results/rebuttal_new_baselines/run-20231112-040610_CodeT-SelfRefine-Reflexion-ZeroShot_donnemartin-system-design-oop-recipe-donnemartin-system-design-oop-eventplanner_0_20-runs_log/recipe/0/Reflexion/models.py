from dataclasses import dataclass

@dataclass
class User:
	id: int
	username: str
	email: str
	favorites: list

@dataclass
class Recipe:
	id: int
	name: str
	ingredients: list
	instructions: str
	image: str
	category: str
	reviews: list

@dataclass
class Review:
	id: int
	user_id: int
	recipe_id: int
	rating: int
	comment: str
