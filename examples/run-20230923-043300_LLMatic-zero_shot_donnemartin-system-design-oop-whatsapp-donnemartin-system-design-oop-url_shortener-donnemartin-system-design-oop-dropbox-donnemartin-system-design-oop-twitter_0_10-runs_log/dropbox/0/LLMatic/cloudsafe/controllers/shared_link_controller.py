from flask import Blueprint, request
from cloudsafe.models.shared_link import SharedLink

shared_link_controller = Blueprint('shared_link_controller', __name__)

@shared_link_controller.route('/generate', methods=['POST'])
def generate_link():
	data = request.get_json()
	shared_link = SharedLink.generate_link(data['file_id'])
	return {'url': shared_link.url}, 201

@shared_link_controller.route('/expiry', methods=['PUT'])
def set_expiry_date():
	data = request.get_json()
	shared_link = SharedLink.set_expiry_date(data['link_id'], data['expiry_date'])
	return {'message': 'Expiry date set successfully'}, 200

@shared_link_controller.route('/password', methods=['PUT'])
def set_password():
	data = request.get_json()
	shared_link = SharedLink.set_password(data['link_id'], data['password'])
	return {'message': 'Password set successfully'}, 200
