from dataclasses import dataclass
from typing import List
from models.tweet import Tweet

@dataclass
class Conversation:
	tweets: List[Tweet]
