from flask import Flask, request, jsonify
from user import User
from service import Service

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
	user_id = request.form['user_id']
	file = request.files['file']
	User(user_id).upload_file(file)
	return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/view', methods=['GET'])
def view():
	user_id = request.args.get('user_id')
	file_id = request.args.get('file_id')
	file = User(user_id).view_file(file_id)
	return jsonify({'file': file}), 200

@app.route('/search', methods=['GET'])
def search():
	user_id = request.args.get('user_id')
	query = request.args.get('query')
	files = User(user_id).search_files(query)
	return jsonify({'files': files}), 200

@app.route('/share', methods=['POST'])
def share():
	user_id = request.form['user_id']
	file_id = request.form['file_id']
	recipient_id = request.form['recipient_id']
	User(user_id).share_file(file_id, recipient_id)
	return jsonify({'message': 'File shared successfully'}), 200

@app.route('/download', methods=['GET'])
def download():
	user_id = request.args.get('user_id')
	file_id = request.args.get('file_id')
	file = User(user_id).download_file(file_id)
	return jsonify({'file': file}), 200

if __name__ == '__main__':
	app.run(debug=True)
