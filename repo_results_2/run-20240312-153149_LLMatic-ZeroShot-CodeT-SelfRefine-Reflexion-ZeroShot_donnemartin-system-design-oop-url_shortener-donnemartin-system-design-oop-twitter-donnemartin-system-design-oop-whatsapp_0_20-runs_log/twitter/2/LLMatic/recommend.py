from user import User, users_db
from post import post_db


def recommend(user):
	recommendations = []
	
	# Recommend users who have a high number of mutual followers with the user
	for other_user in users_db.values():
		if other_user != user:
			mutual_followers = set(user.followers).intersection(set(other_user.followers))
			if len(mutual_followers) > 2:
				recommendations.append(other_user)
	
	# Recommend users who post about similar topics as the user
	user_posts = ' '.join([post.text for post in user.posts])
	for other_user in users_db.values():
		if other_user != user:
			other_user_posts = ' '.join([post.text for post in other_user.posts])
			if len(set(user_posts.split()).intersection(set(other_user_posts.split()))) > 2:
				recommendations.append(other_user)
	
	# Recommend users who have a high level of activity
	for other_user in users_db.values():
		if other_user != user and len(other_user.posts) > 5:
			recommendations.append(other_user)
	
	return list(set(recommendations))

