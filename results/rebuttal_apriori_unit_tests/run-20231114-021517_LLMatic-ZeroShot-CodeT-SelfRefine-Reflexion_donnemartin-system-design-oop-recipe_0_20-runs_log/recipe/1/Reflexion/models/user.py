import dataclasses

@dataclasses.dataclass
class User:
	id: str
	username: str
	password: str
	favorite_recipes: list
	followed_users: list
