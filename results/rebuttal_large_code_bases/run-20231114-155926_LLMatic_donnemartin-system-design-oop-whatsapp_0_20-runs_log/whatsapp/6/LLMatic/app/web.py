from flask import Blueprint, render_template, request

web = Blueprint('web', __name__)

@web.route('/')
def home():
	return render_template('home.html')

@web.route('/chat')
def chat():
	return render_template('chat.html')

@web.route('/feedback', methods=['GET', 'POST'])
def feedback():
	if request.method == 'POST':
		feedback_data = request.form
		from .feedback import store_feedback
		store_feedback(feedback_data)
		return 'Thank you for your feedback!'
	return render_template('feedback.html')
