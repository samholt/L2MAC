import jwt
from dataclasses import dataclass, field
from typing import Dict, Optional, List

# Mock database
users_db: Dict[str, 'User'] = {}

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: Optional[str] = None
	bio: Optional[str] = None
	website_link: Optional[str] = None
	location: Optional[str] = None
	visibility: str = 'public'
	following: List[str] = field(default_factory=list)
	followers: List[str] = field(default_factory=list)


def register_user(email: str, username: str, password: str) -> User:
	"""Register a new user."""
	user = User(email, username, password)
	users_db[username] = user
	return user


def authenticate_user(username: str, password: str) -> str:
	"""Authenticate a user and return a JWT."""
	user = users_db.get(username)
	if user is None or user.password != password:
		return ''
	# Create a JWT
	token = jwt.encode({'username': username}, 'secret', algorithm='HS256')
	return token

def update_profile(username: str, profile_picture: Optional[str], bio: Optional[str], website_link: Optional[str], location: Optional[str], visibility: str) -> User:
	"""Update a user's profile."""
	user = users_db.get(username)
	if user is None:
		return None
	user.profile_picture = profile_picture
	user.bio = bio
	user.website_link = website_link
	user.location = location
	user.visibility = visibility
	return user

def follow_user(username: str, user_to_follow: str) -> bool:
	"""Follow a user."""
	user = users_db.get(username)
	if user is None or user_to_follow not in users_db:
		return False
	user.following.append(user_to_follow)
	users_db[user_to_follow].followers.append(username)
	return True

def unfollow_user(username: str, user_to_unfollow: str) -> bool:
	"""Unfollow a user."""
	user = users_db.get(username)
	if user is None or user_to_unfollow not in users_db or user_to_unfollow not in user.following:
		return False
	user.following.remove(user_to_unfollow)
	users_db[user_to_unfollow].followers.remove(username)
	return True
