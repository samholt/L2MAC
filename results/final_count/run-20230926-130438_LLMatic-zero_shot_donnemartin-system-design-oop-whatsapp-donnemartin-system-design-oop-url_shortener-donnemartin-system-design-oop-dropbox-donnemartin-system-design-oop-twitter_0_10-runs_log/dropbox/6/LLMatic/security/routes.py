from flask import Blueprint, request
import hashlib

security_bp = Blueprint('security', __name__)

activity_log = []

@security_bp.route('/encrypt', methods=['POST'])
def encrypt():
	data = request.get_json()
	encrypted_data = hashlib.sha256(data['file'].encode()).hexdigest()
	activity_log.append({'action': 'encrypt', 'file': data['file']})
	return {'encrypted_file': encrypted_data}

@security_bp.route('/decrypt', methods=['POST'])
def decrypt():
	data = request.get_json()
	decrypted_data = data['file']
	activity_log.append({'action': 'decrypt', 'file': data['file']})
	return {'decrypted_file': decrypted_data}

@security_bp.route('/activity_log')
def get_activity_log():
	return {'activity_log': activity_log}
