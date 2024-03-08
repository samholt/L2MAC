from dataclasses import dataclass
from typing import List

@dataclass
class Group:
	id: int
	name: str
	picture: str
	participants: List[int]
	admins: List[int]
