from flask import Blueprint, request
from datetime import datetime, timedelta
import uuid

file_sharing = Blueprint('file_sharing', __name__)

share_links = {}

@file_sharing.route('/share', methods=['POST'])
def share():
	data = request.get_json()
	file_id = data.get('file_id')
	expiry_date = data.get('expiry_date')
	password = data.get('password')
	
	if not file_id:
		return {'message': 'File id is required'}, 400
	
	link_id = str(uuid.uuid4())
	expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d') if expiry_date else datetime.now() + timedelta(days=7)
	share_links[link_id] = {'file_id': file_id, 'expiry_date': expiry_date, 'password': password}
	
	return {'message': 'Share link generated', 'link_id': link_id}, 200

@file_sharing.route('/invite', methods=['POST'])
def invite():
	data = request.get_json()
	email = data.get('email')
	folder_id = data.get('folder_id')
	permissions = data.get('permissions')
	
	if not email or not folder_id or not permissions:
		return {'message': 'Email, folder id and permissions are required'}, 400
	
	# Here we would normally send an email to the user with the invitation and permissions
	# But for this task, we will just return a success message
	
	return {'message': 'Invitation sent'}, 200
