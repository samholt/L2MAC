from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User

app = Flask(__name__)

@app.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
	data = request.get_json()
	user_email = get_jwt_identity()['email']
	user = User.query.filter_by(email=user_email).first()
	if user:
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		user.is_private = data.get('is_private', user.is_private)
		db.session.commit()
		return jsonify({'message': 'Profile updated successfully'}), 200
	else:
		return jsonify({'message': 'User not found'}), 404
