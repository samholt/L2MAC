from dataclasses import dataclass, field
from typing import List

@dataclass
class Transaction:
	id: str
	amount: float
	category: str

@dataclass
class User:
	id: str
	username: str
	password: str
	transactions: List[Transaction] = field(default_factory=list)
