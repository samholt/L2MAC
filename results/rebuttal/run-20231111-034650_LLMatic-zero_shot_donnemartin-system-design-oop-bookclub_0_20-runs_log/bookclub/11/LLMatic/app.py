from flask import Flask, request
from resource import Resource
from book_club import BookClub

app = Flask(__name__)
resource = Resource()
book_club = BookClub()

@app.route('/add_resource', methods=['POST'])
def add_resource():
	data = request.get_json()
	resource.add_resource(data['title'], data['content'])
	return {'message': 'Resource added successfully'}, 200

@app.route('/view_resources', methods=['GET'])
def view_resources():
	return resource.view_resources(), 200

@app.route('/book_club', methods=['POST'])
def create_club():
	data = request.get_json()
	message = book_club.create_club(data['name'], data['description'], data['privacy'])
	return {'message': message}, 200

@app.route('/book_club/join', methods=['POST'])
def join_club():
	data = request.get_json()
	message = book_club.join_club(data['name'], data['user'])
	return {'message': message}, 200

@app.route('/book_club/manage', methods=['POST'])
def manage_request():
	data = request.get_json()
	message = book_club.manage_request(data['name'], data['user'], data['action'])
	return {'message': message}, 200

if __name__ == '__main__':
	app.run(debug=True)
