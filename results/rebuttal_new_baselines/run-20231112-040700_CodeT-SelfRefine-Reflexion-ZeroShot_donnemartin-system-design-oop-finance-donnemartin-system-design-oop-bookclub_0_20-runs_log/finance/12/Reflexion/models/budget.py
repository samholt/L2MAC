from dataclasses import dataclass

@dataclasses.dataclass
class Budget:
	id: int
	user_id: int
	category: str
	limit: float
