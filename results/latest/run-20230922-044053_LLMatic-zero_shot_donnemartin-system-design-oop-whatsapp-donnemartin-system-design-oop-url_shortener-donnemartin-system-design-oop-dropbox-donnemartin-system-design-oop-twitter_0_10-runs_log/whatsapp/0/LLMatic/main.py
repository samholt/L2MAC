from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import LoginForm, RegistrationForm, ProfileForm, ContactForm, MessageForm
from models import User, Contact, Message
from flask_login import current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)

import models

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid email or password')
			return redirect(url_for('login'))
		login_user(user)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	form = ProfileForm()
	if form.validate_on_submit():
		if form.profile_picture.data:
			current_user.set_profile_picture(form.profile_picture.data)
		if form.status_message.data:
			current_user.set_status_message(form.status_message.data)
		if form.privacy_settings.data:
			current_user.update_privacy_settings(form.privacy_settings.data)
		db.session.commit()
		flash('Your changes have been saved.')
		return redirect(url_for('profile'))
	return render_template('profile.html', title='Profile', form=form)

@app.route('/contacts', methods=['GET', 'POST'])
@login_required
def contacts():
	form = ContactForm()
	if form.validate_on_submit():
		contact = Contact.query.filter_by(user_id=current_user.id, contact_id=form.contact_id.data).first()
		if contact is None:
			contact = Contact(user_id=current_user.id, contact_id=form.contact_id.data)
			current_user.contacts.append(contact)
		contact.blocked = form.blocked.data
		db.session.commit()
		flash('Your changes have been saved.')
		return redirect(url_for('contacts'))
	return render_template('contacts.html', title='Contacts', form=form)

@app.route('/send_message', methods=['GET', 'POST'])
@login_required
def send_message():
	form = MessageForm()
	if form.validate_on_submit():
		recipient = User.query.filter_by(id=form.recipient.data).first()
		if recipient:
			current_user.send_message(recipient, form.text.data)
			flash('Your message has been sent.')
			return redirect(url_for('send_message'))
		else:
			flash('Invalid recipient.')
	return render_template('send_message.html', title='Send Message', form=form)

@socketio.on('message')
def handle_message(msg):
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app, debug=True)
