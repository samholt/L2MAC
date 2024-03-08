from flask import Blueprint, request
from cloudsafe.models.shared_folder import SharedFolder

shared_folder_controller = Blueprint('shared_folder_controller', __name__)

@shared_folder_controller.route('/invite', methods=['POST'])
def invite_user():
	data = request.get_json()
	shared_folder = SharedFolder.invite_user(data['folder_id'], data['user_id'])
	return {'message': 'User invited successfully'}, 201

@shared_folder_controller.route('/permissions', methods=['PUT'])
def set_permissions():
	data = request.get_json()
	shared_folder = SharedFolder.set_permissions(data['folder_id'], data['user_id'], data['permissions'])
	return {'message': 'Permissions set successfully'}, 200
