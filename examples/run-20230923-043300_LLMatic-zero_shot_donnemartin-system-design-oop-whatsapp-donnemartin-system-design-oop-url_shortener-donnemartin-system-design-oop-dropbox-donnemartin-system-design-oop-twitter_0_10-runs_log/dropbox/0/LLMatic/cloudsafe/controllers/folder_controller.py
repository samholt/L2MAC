from flask import Blueprint, request
from cloudsafe.models.folder import Folder

folder_controller = Blueprint('folder_controller', __name__)

@folder_controller.route('/create', methods=['POST'])
def create():
	data = request.get_json()
	folder = Folder.create(data['name'])
	return {'message': 'Folder created successfully'}, 201

@folder_controller.route('/rename', methods=['PUT'])
def rename():
	data = request.get_json()
	folder = Folder.rename(data['folder_id'], data['new_name'])
	return {'message': 'Folder renamed successfully'}, 200

@folder_controller.route('/move', methods=['PUT'])
def move():
	data = request.get_json()
	folder = Folder.move(data['folder_id'], data['new_location'])
	return {'message': 'Folder moved successfully'}, 200

@folder_controller.route('/delete', methods=['DELETE'])
def delete():
	data = request.get_json()
	folder = Folder.delete(data['folder_id'])
	return {'message': 'Folder deleted successfully'}, 200
