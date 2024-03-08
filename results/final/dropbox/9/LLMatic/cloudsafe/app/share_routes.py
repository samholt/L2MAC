from flask import Blueprint, request, jsonify
from . import db
from .models import User, File
import uuid


share_bp = Blueprint('share', __name__)


@share_bp.route('/share-link', methods=['POST'])
def share_link():
	data = request.get_json()
	file = File.query.filter_by(filename=data['filename']).first()
	if file:
		file.share_id = str(uuid.uuid4())
		db.session.commit()
		return jsonify({'share_link': '/download/' + file.share_id}), 200
	return jsonify({'message': 'File not found'}), 404


@share_bp.route('/share-folder', methods=['POST'])
def share_folder():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user:
		user.shared_folders.append(data['folder'])
		db.session.commit()
		return jsonify({'message': 'Folder shared successfully'}), 200
	return jsonify({'message': 'User not found'}), 404
