from flask import Blueprint, request
from cloudsafe.app.sharing_service import SharingService

sharing = Blueprint('sharing', __name__)
sharing_service = SharingService()

@sharing.route('/generate_share_link', methods=['POST'])
def generate_share_link():
	data = request.get_json()
	response = sharing_service.generate_share_link(**data)
	return {'message': response}, 200

@sharing.route('/set_expiry_date', methods=['PUT'])
def set_expiry_date():
	data = request.get_json()
	response = sharing_service.set_expiry_date(**data)
	return {'message': response}, 200

@sharing.route('/set_password', methods=['PUT'])
def set_password():
	data = request.get_json()
	response = sharing_service.set_password(**data)
	return {'message': response}, 200

@sharing.route('/invite_user', methods=['POST'])
def invite_user():
	data = request.get_json()
	response = sharing_service.invite_user(**data)
	return {'message': response}, 200

@sharing.route('/set_permissions', methods=['PUT'])
def set_permissions():
	data = request.get_json()
	response = sharing_service.set_permissions(**data)
	return {'message': response}, 200
