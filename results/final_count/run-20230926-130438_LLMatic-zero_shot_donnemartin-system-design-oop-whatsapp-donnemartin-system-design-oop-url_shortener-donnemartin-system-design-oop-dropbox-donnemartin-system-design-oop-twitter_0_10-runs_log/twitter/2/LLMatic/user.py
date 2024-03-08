from dataclasses import dataclass, field
import jwt

# Mock database
users_db = {}

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	is_private: bool = False
	following: list = field(default_factory=list)
	followers: list = field(default_factory=list)
	blocked_users: list = field(default_factory=list)
	notifications: list = field(default_factory=list)


def register_user(email: str, username: str, password: str) -> str:
	if email in [user.email for user in users_db.values()] or username in users_db:
		return 'Email or username already taken'
	else:
		users_db[username] = User(email, username, password)
		return 'User registered successfully'


def authenticate_user(username: str, password: str) -> str:
	if username in users_db and users_db[username].password == password:
		# Generate JWT token
		token = jwt.encode({'username': username}, 'secret', algorithm='HS256')
		return token
	else:
		return 'Invalid credentials'


def edit_profile(username: str, profile_picture: str, bio: str, website_link: str, location: str, is_private: bool):
	if username in users_db:
		user = users_db[username]
		user.profile_picture = profile_picture
		user.bio = bio
		user.website_link = website_link
		user.location = location
		user.is_private = is_private
		users_db[username] = user
		return 'Profile updated successfully'
	else:
		return 'User not found'


def search_users(keyword: str) -> list:
	# Search for users that match the keyword
	matching_users = [user for user in users_db.values() if keyword in user.username or keyword in user.bio]
	return matching_users


def follow_user(username: str, user_to_follow: str) -> str:
	if username in users_db and user_to_follow in users_db:
		user = users_db[username]
		user_to_follow_instance = users_db[user_to_follow]
		if user_to_follow not in user.following:
			user.following.append(user_to_follow)
			user_to_follow_instance.followers.append(username)
			users_db[username] = user
			users_db[user_to_follow] = user_to_follow_instance
			return 'User followed successfully'
		else:
			return 'User already followed'
	else:
		return 'User not found'


def unfollow_user(username: str, user_to_unfollow: str) -> str:
	if username in users_db and user_to_unfollow in users_db:
		user = users_db[username]
		user_to_unfollow_instance = users_db[user_to_unfollow]
		if user_to_unfollow in user.following:
			user.following.remove(user_to_unfollow)
			user_to_unfollow_instance.followers.remove(username)
			users_db[username] = user
			users_db[user_to_unfollow] = user_to_unfollow_instance
			return 'User unfollowed successfully'
		else:
			return 'User not followed'
	else:
		return 'User not found'


def add_notification(username: str, notification: str) -> str:
	if username in users_db:
		user = users_db[username]
		user.notifications.append(notification)
		users_db[username] = user
		return 'Notification added'
	else:
		return 'User not found'

