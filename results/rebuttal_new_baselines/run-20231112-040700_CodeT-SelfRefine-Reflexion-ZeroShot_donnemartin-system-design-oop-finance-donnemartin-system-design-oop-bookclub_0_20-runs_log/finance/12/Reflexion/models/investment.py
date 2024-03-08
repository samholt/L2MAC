from dataclasses import dataclass

@dataclasses.dataclass
class Investment:
	id: int
	user_id: int
	value: float
	roi: float
