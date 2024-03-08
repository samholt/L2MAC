from flask import Blueprint, request
from cloudsafe.app.file_service import FileService

file_blueprint = Blueprint('file', __name__)
file_service = FileService()

@file_blueprint.route('/upload', methods=['POST'])
def upload_file():
	data = request.get_json()
	response = file_service.upload_file(data['id'], data['name'], data['user_id'], data['folder_id'])
	return {'message': response}, 200

@file_blueprint.route('/download/<id>', methods=['GET'])
def download_file(id):
	response = file_service.download_file(id)
	return {'message': response}, 200

@file_blueprint.route('/move/<id>', methods=['PUT'])
def move_file(id):
	data = request.get_json()
	response = file_service.move_file(id, data['new_folder_id'])
	return {'message': response}, 200

@file_blueprint.route('/rename/<id>', methods=['PUT'])
def rename_file(id):
	data = request.get_json()
	response = file_service.rename_file(id, data['new_name'])
	return {'message': response}, 200

@file_blueprint.route('/delete/<id>', methods=['DELETE'])
def delete_file(id):
	response = file_service.delete_file(id)
	return {'message': response}, 200

@file_blueprint.route('/folder/create', methods=['POST'])
def create_folder():
	data = request.get_json()
	response = file_service.create_folder(data['id'], data['name'], data['user_id'], data['parent_folder_id'])
	return {'message': response}, 200

@file_blueprint.route('/folder/rename/<id>', methods=['PUT'])
def rename_folder(id):
	data = request.get_json()
	response = file_service.rename_folder(id, data['new_name'])
	return {'message': response}, 200

@file_blueprint.route('/folder/move/<id>', methods=['PUT'])
def move_folder(id):
	data = request.get_json()
	response = file_service.move_folder(id, data['new_parent_folder_id'])
	return {'message': response}, 200

@file_blueprint.route('/folder/delete/<id>', methods=['DELETE'])
def delete_folder(id):
	response = file_service.delete_folder(id)
	return {'message': response}, 200
