from flask import render_template, request, Blueprint
from flask_login import login_required
from app.models import Message

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
	page = request.args.get('page', 1, type=int)
	messages = Message.query.order_by(Message.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', messages=messages)
