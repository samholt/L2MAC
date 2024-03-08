from dataclasses import dataclass

@dataclass
class ShareableLink:
	url: str
	expiry_date: str
	password: str

links = {}

def share(data):
	link = ShareableLink(**data)
	links[link.url] = link
	return link
