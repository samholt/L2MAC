from flask import Blueprint, request, jsonify
from .models import User
from app import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/block', methods=['POST'])
def block_contact():
	user_id = request.json.get('user_id')
	contact_id = request.json.get('contact_id')
	user = db.session.query(User).filter_by(id=user_id).first()
	contact = db.session.query(User).filter_by(id=contact_id).first()
	if not user or not contact:
		return jsonify({'message': 'User or contact not found'}), 404
	user.block_contact(contact)
	return jsonify({'message': 'Contact blocked successfully'}), 200

@contacts.route('/unblock', methods=['POST'])
def unblock_contact():
	user_id = request.json.get('user_id')
	contact_id = request.json.get('contact_id')
	user = db.session.query(User).filter_by(id=user_id).first()
	contact = db.session.query(User).filter_by(id=contact_id).first()
	if not user or not contact:
		return jsonify({'message': 'User or contact not found'}), 404
	user.unblock_contact(contact)
	return jsonify({'message': 'Contact unblocked successfully'}), 200
