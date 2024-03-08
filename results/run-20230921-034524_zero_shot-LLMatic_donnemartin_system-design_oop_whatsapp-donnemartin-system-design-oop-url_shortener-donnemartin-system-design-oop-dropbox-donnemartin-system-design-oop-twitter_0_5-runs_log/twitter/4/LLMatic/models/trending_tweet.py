from dataclasses import dataclass
from models.tweet import Tweet

@dataclass
class TrendingTweet:
	tweet: Tweet
	popularity: int
