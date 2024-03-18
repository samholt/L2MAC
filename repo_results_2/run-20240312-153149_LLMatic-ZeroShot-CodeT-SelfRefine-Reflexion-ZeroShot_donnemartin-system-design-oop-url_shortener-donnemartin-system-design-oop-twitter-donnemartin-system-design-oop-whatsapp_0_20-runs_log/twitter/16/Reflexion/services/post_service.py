from models.post import Post

posts = {}

def create_post(user, content, images=[]):
	post = Post(user, content, images=images)
	posts[user.email] = post
	return post

def get_post(user):
	return posts.get(user.email, None)

def delete_post(user):
	posts.pop(user.email, None)
