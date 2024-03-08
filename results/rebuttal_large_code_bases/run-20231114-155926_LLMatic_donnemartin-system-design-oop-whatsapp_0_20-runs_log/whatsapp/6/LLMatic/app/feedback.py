from flask import Blueprint, request
from app.models import Feedback, db

feedback = Blueprint('feedback', __name__)

@feedback.route('/store', methods=['POST'])

def store_feedback():
	feedback_data = request.get_json()
	new_feedback = Feedback(user_id=feedback_data['user_id'], feedback=feedback_data['feedback'])
	db.session.add(new_feedback)
	db.session.commit()
	return {'id': new_feedback.id}, 201

@feedback.route('/', methods=['GET'])

def get_feedbacks():
	feedbacks = Feedback.query.all()
	return {'feedbacks': [f.feedback for f in feedbacks]}, 200
