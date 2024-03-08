from flask import Blueprint, request, jsonify
from cloudsafe.app.models import User, db, Activity
from flask_login import current_user
from datetime import datetime


bp = Blueprint('routes', __name__)


@bp.route('/change-password', methods=['POST'])
def change_password():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and user.check_password(data['old_password']):
		user.set_password(data['new_password'])
		db.session.commit()
		return jsonify({'message': 'Password changed successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401


@bp.route('/activity', methods=['GET'])
def activity():
	activities = Activity.query.filter_by(user_id=current_user.id).order_by(Activity.timestamp.desc()).all()
	return jsonify([activity.to_dict() for activity in activities]), 200
