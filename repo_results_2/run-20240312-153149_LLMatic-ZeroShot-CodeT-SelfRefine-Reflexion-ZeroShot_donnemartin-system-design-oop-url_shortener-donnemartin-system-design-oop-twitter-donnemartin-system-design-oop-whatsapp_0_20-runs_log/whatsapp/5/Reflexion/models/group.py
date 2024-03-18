from dataclasses import dataclass
from typing import List

@dataclass
class Group:
	id: str
	name: str
	admin_id: str
	participants: List[str]
