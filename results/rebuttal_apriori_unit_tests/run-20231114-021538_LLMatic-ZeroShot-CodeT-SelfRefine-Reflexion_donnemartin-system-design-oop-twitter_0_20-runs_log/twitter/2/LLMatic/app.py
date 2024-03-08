from flask import Flask, request
from views import search_posts, search_users

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/search/posts', methods=['GET'])
def search_posts_endpoint():
	keyword = request.args.get('keyword')
	results = search_posts(keyword)
	return {'results': [post.__dict__ for post in results]}

@app.route('/search/users', methods=['GET'])
def search_users_endpoint():
	keyword = request.args.get('keyword')
	results = search_users(keyword)
	return {'results': [user.__dict__ for user in results]}

if __name__ == '__main__':
	app.run()

