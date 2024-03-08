from dataclasses import dataclass
from typing import List

@dataclass
class User:
	username: str
	password: str
	followers: List['User']
	following: List['User']
