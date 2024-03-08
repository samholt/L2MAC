from dataclasses import dataclass

@dataclass
class Trending:
	id: int
	topic: str
	mentions: int
