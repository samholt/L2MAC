from flask import Blueprint, request
from .models import File

file_blueprint = Blueprint('file', __name__)

@file_blueprint.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']
	new_file = File(name=file.filename, size=file.content_length, type=file.content_type, upload_date=None, version=1, parent_folder=None)
	new_file.upload(file)
	return {'message': 'File uploaded successfully'}, 200

@file_blueprint.route('/download/<file_id>', methods=['GET'])
def download(file_id):
	file = File.query.get(file_id)
	if file:
		return file.download()
	else:
		return {'message': 'File not found'}, 404

@file_blueprint.route('/organize/<file_id>', methods=['PUT'])
def organize(file_id):
	file = File.query.get(file_id)
	if file:
		data = request.json
		file.rename(data['new_name'])
		file.move(data['new_folder'])
		return {'message': 'File organized successfully'}, 200
	else:
		return {'message': 'File not found'}, 404

@file_blueprint.route('/versioning/<file_id>', methods=['PUT'])
def versioning(file_id):
	file = File.query.get(file_id)
	if file:
		data = request.json
		file.versioning(data['new_version'])
		return {'message': 'File version updated successfully'}, 200
	else:
		return {'message': 'File not found'}, 404
