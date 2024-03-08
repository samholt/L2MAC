from flask import Flask, request, jsonify
from user import User
from file_manager import FileManager

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User()
	response = user.register(data)
	return jsonify(response)

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User()
	response = user.login(data)
	return jsonify(response)

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file_manager = FileManager()
	response = file_manager.upload(data)
	return jsonify(response)

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	file_manager = FileManager()
	response = file_manager.download(data)
	return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)
