from dataclasses import dataclass, field
from typing import List

@dataclass
class Recipe:
	id: int
	name: str
	ingredients: List[str]
	instructions: List[str]
	image: str
	categories: List[str]

@dataclass
class User:
	id: int
	name: str
	favorites: List[int] = field(default_factory=list)
