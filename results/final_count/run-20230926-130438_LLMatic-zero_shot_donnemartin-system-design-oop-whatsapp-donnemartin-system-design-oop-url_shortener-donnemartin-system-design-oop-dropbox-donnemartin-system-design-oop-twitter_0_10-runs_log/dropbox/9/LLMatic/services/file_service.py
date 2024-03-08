import os
import json
from models.file import File
import base64

# Mock database
files_db = {}

# Encryption key
key = b'Sixteen byte key'

# Activity log
activity_log = []

def encrypt_file_content(content):
	enc_content = base64.b64encode(content.encode())
	return enc_content

def decrypt_file_content(enc_content):
	dec_content = base64.b64decode(enc_content).decode()
	return dec_content

def upload_file(file):
	file.content = encrypt_file_content(file.content)
	files_db[file.id] = file
	activity_log.append(f'File with id {file.id} uploaded by user {file.owner}')

def download_file(file_id, user_id):
	file = files_db.get(file_id)
	if file and file.owner == user_id:
		activity_log.append(f'File with id {file.id} downloaded by user {user_id}')
		return decrypt_file_content(file.content)
	else:
		return None

def delete_file(file_id, user_id):
	file = files_db.get(file_id)
	if file and file.owner == user_id:
		activity_log.append(f'File with id {file.id} deleted by user {user_id}')
		del files_db[file_id]

def share_file(file_id, user_id, target_user_id):
	file = files_db.get(file_id)
	if file and file.owner == user_id:
		activity_log.append(f'File with id {file.id} shared by user {user_id} with user {target_user_id}')
		file.shared_with.append(target_user_id)

def get_activity_log():
	return activity_log
