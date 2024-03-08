from flask import Blueprint, request
from cloudsafe.app.security_service import SecurityService

security_blueprint = Blueprint('security', __name__)

@security_blueprint.route('/encrypt', methods=['POST'])
def encrypt_file():
	file = request.files['file']
	SecurityService.encrypt_file(file)
	return {'message': 'File encrypted successfully'}, 200

@security_blueprint.route('/decrypt', methods=['POST'])
def decrypt_file():
	file = request.files['file']
	SecurityService.decrypt_file(file)
	return {'message': 'File decrypted successfully'}, 200

@security_blueprint.route('/log', methods=['GET'])
def get_activity_log():
	user_id = request.args.get('user_id')
	logs = SecurityService.get_activity_log(user_id)
	return {'logs': logs}, 200
