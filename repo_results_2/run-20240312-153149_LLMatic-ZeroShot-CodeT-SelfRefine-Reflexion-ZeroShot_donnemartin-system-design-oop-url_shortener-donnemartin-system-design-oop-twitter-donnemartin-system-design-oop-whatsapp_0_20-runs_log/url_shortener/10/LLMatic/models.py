from dataclasses import dataclass

@dataclass
class URL:
	original_url: str
	shortened_url: str
	user: str
