from flask import Blueprint, request, send_file, abort
from . import db
from .models import File, User
from io import BytesIO


file_bp = Blueprint('file', __name__)


@file_bp.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['file']
	user = User.query.filter_by(username=request.form['username']).first()
	existing_file = File.query.filter_by(filename=file.filename).first()
	if existing_file:
		existing_file.versions.append(existing_file.data)
		existing_file.data = file.read()
	else:
		new_file = File(filename=file.filename, data=file.read(), owner=user)
		db.session.add(new_file)
	db.session.commit()
	return '', 204


@file_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
	version = request.args.get('version')
	file = File.query.filter_by(filename=filename).first()
	if file:
		if version is not None:
			version = int(version)
			if version < len(file.versions):
				return send_file(BytesIO(file.versions[version]), attachment_filename=filename)
			else:
				abort(404)
		else:
			return send_file(BytesIO(file.data), attachment_filename=filename)
	else:
		abort(404)

