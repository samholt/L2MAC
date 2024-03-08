from flask import Blueprint, request, send_file
from .models import File, Folder
from io import BytesIO

file_management = Blueprint('file_management', __name__)

files_db = {}
folders_db = {}

@file_management.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		files_db[file.filename] = File(file.filename, file.content_type, file.content_length, file.read(), 1)
		return 'File uploaded successfully'
	else:
		return '<form method="POST" enctype="multipart/form-data"><input type="file" name="file"><input type="submit" value="Upload"></form>'

@file_management.route('/download/<filename>', methods=['GET'])
def download_file(filename):
	file = files_db.get(filename)
	if file:
		return send_file(BytesIO(file.content), as_attachment=True, mimetype=file.file_type, download_name=file.name)
	else:
		return 'File not found'

@file_management.route('/create_folder/<foldername>', methods=['GET'])
def create_folder(foldername):
	folders_db[foldername] = Folder(foldername, {})
	return 'Folder created successfully'

@file_management.route('/rename_file/<filename>/<newname>', methods=['GET'])
def rename_file(filename, newname):
	file = files_db.get(filename)
	if file:
		file.name = newname
		files_db[newname] = files_db.pop(filename)
		return 'File renamed successfully'
	else:
		return 'File not found'

@file_management.route('/move_file/<filename>/<foldername>', methods=['GET'])
def move_file(filename, foldername):
	file = files_db.get(filename)
	folder = folders_db.get(foldername)
	if file and folder:
		folder.files[filename] = file
		files_db.pop(filename)
		return 'File moved successfully'
	else:
		return 'File or folder not found'

@file_management.route('/delete_file/<filename>', methods=['GET'])
def delete_file(filename):
	file = files_db.pop(filename, None)
	if file:
		return 'File deleted successfully'
	else:
		return 'File not found'

@file_management.route('/restore_file/<filename>/<version>', methods=['GET'])
def restore_file(filename, version):
	file = files_db.get(filename)
	if file and file.version >= int(version):
		file.version = int(version)
		return 'File restored to version ' + version
	else:
		return 'File not found or invalid version'

