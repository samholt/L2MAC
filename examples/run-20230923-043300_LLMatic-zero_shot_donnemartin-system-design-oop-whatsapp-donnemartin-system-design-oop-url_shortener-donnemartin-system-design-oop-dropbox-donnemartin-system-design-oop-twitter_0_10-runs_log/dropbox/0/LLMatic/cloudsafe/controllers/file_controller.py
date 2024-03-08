from flask import Blueprint, request
from cloudsafe.models.file import File

file_controller = Blueprint('file_controller', __name__)

@file_controller.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = File.upload(data['file'])
	return {'message': 'File uploaded successfully'}, 201

@file_controller.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	file = File.download(data['file_id'])
	return {'file': file}, 200

@file_controller.route('/rename', methods=['PUT'])
def rename():
	data = request.get_json()
	file = File.rename(data['file_id'], data['new_name'])
	return {'message': 'File renamed successfully'}, 200

@file_controller.route('/move', methods=['PUT'])
def move():
	data = request.get_json()
	file = File.move(data['file_id'], data['new_location'])
	return {'message': 'File moved successfully'}, 200

@file_controller.route('/delete', methods=['DELETE'])
def delete():
	data = request.get_json()
	file = File.delete(data['file_id'])
	return {'message': 'File deleted successfully'}, 200
