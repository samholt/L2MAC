from dataclasses import dataclass

@dataclasses.dataclass
class Transaction:
	id: int
	user_id: int
	account_id: int
	amount: float
	category: str
	is_recurring: bool
