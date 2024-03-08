from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class URL:
	original_url: str
	shortened_url: str
	clicks: int = 0
	click_dates: List[str] = field(default_factory=list)
	click_geolocations: List[Dict[str, str]] = field(default_factory=list)
