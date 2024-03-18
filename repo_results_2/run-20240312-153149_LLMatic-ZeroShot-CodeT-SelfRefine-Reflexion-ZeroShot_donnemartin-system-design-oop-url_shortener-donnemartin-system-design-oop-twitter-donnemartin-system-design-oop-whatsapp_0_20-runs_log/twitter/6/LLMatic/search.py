def search(keyword, db):
	results = {'users': [], 'posts': []}
	for user in db.values():
		if keyword in user.username or keyword in user.bio:
			results['users'].append(user)
		for post in user.posts:
			if keyword in post.content:
				results['posts'].append(post)
	return results

def filter(tag, db):
	results = []
	for user in db.values():
		for post in user.posts:
			if tag in post.content:
				results.append(post)
	return results
