import dataclasses

@dataclasses.dataclass
class Recipe:
	id: str
	name: str
	ingredients: list
	instructions: list
	images: list
	categories: list
	user_id: str
	ratings: list
	reviews: list
