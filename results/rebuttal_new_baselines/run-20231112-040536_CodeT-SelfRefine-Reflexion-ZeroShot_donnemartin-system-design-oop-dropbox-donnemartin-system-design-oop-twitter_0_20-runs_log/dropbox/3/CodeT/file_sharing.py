from dataclasses import dataclass

@dataclass
class Link:
	url: str
	expiry_date: str
	password: str

links = {}


def generate_link(data):
	link = Link(**data)
	links[link.url] = link
	return {'message': 'Link generated successfully'}, 201

def invite_user(data):
	# Placeholder for user invitation
	return {'message': 'User invited successfully'}, 201

def set_permission(data):
	# Placeholder for setting permissions
	return {'message': 'Permission set successfully'}, 201
