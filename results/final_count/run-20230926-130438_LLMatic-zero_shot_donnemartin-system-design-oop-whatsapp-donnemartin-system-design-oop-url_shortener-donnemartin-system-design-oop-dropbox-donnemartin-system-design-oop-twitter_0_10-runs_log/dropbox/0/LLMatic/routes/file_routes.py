from flask import Blueprint, request
from services.file_service import FileService

file_service = FileService()

file_routes = Blueprint('file_routes', __name__)

@file_routes.route('/files')
def get_files():
	return 'Get Files'

@file_routes.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['file']
	user = request.form['user']
	new_file = file_service.upload_file(file, user)
	return new_file, 201

@file_routes.route('/download/<int:file_id>', methods=['GET'])
def download_file(file_id):
	file = file_service.download_file(file_id)
	return file

@file_routes.route('/create_folder', methods=['POST'])
def create_folder():
	folder_name = request.form['folder_name']
	user = request.form['user']
	new_folder = file_service.create_folder(folder_name, user)
	return new_folder, 201

@file_routes.route('/rename/<int:file_id>', methods=['PUT'])
def rename_file(file_id):
	new_name = request.form['new_name']
	file = file_service.rename_file(file_id, new_name)
	return file

@file_routes.route('/move/<int:file_id>', methods=['PUT'])
def move_file(file_id):
	new_path = request.form['new_path']
	file = file_service.move_file(file_id, new_path)
	return file

@file_routes.route('/delete/<int:file_id>', methods=['DELETE'])
def delete_file(file_id):
	message = file_service.delete_file(file_id)
	return message

@file_routes.route('/share/<int:file_id>', methods=['GET'])
def share_file(file_id):
	link = file_service.generate_shareable_link(file_id)
	return link
