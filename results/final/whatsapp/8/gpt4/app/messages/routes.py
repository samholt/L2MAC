from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from app import db
from app.models import Message
from app.messages.forms import MessageForm

messages = Blueprint('messages', __name__)

@messages.route("/message/new", methods=['GET', 'POST'])
@login_required
def new_message():
	form = MessageForm()
	if form.validate_on_submit():
		message = Message(content=form.content.data, author=current_user)
		db.session.add(message)
		db.session.commit()
		flash('Your message has been sent!', 'success')
		return redirect(url_for('main.home'))
	return render_template('create_message.html', title='New Message', form=form, legend='New Message')
