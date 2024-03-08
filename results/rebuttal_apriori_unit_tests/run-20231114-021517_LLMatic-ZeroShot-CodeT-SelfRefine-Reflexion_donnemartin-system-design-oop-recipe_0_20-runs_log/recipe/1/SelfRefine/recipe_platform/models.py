from dataclasses import dataclass


@dataclass
class User:
	id: int
	username: str
	password: str
	favorites: list
	submitted_recipes: list
	following: list


@dataclass
class Admin(User):
	pass


@dataclass
class Recipe:
	id: int
	title: str
	ingredients: list
	instructions: str
	image: str
	categories: list


@dataclass
class Rating:
	recipe_id: int
	rating: int


@dataclass
class Review:
	recipe_id: int
	review: str


@dataclass
class Activity:
	user_id: int
	activity_type: str
	activity_data: dict
