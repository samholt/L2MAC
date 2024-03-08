from dataclasses import dataclass

@dataclasses.dataclass
class Account:
	id: int
	user_id: int
	balance: float
