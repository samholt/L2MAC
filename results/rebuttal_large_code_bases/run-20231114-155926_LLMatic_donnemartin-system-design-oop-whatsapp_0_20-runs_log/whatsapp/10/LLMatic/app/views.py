from flask import render_template, url_for, flash, redirect, request, abort
from app import app
from app.forms import RegistrationForm, LoginForm, PasswordRecoveryForm, ProfileForm, PrivacyForm, ContactForm, BlockForm, GroupForm, AdminForm, MessageForm, ImageForm, StatusForm
from app.models import User, Group, Message, Status
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime, timedelta

# Mocking a database with an in memory dictionary
users_db = {}
groups_db = {}
messages_db = {}
statuses_db = {}

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# Registration logic here
		flash('Account created for {form.email.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# Authentication logic here
		flash('Login successful for {form.email.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route("/recover_password", methods=['GET', 'POST'])
def recover_password():
	form = PasswordRecoveryForm()
	if form.validate_on_submit():
		# Password recovery logic here
		flash('Password recovery email has been sent!', 'success')
		return redirect(url_for('login'))
	return render_template('recover_password.html', title='Recover Password', form=form)

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
	form = ProfileForm()
	if form.validate_on_submit():
		if form.profile_picture.data:
			current_user.profile_picture = form.profile_picture.data
		if form.status_message.data:
			current_user.status_message = form.status_message.data
		if form.privacy_settings.data:
			current_user.privacy_settings = form.privacy_settings.data
		current_user.last_seen = datetime.utcnow()
		flash('Your profile has been updated!', 'success')
		return redirect(url_for('profile'))
	elif request.method == 'GET':
		form.status_message.data = current_user.status_message
		form.privacy_settings.data = current_user.privacy_settings
	statuses = [status for status in statuses_db.values() if status.user == current_user.username and status.expiry_time > datetime.utcnow()]
	return render_template('profile.html', title='Profile', form=form, statuses=statuses, static_url_path=url_for('static', filename=''))

@app.route("/status", methods=['POST'])
@login_required
def status():
	form = StatusForm()
	if form.validate_on_submit():
		content = form.content.data
		visibility = form.visibility.data
		expiry_time = datetime.utcnow() + timedelta(hours=24)  # Statuses expire after 24 hours
		new_status = Status.create(id=len(statuses_db)+1, user=current_user.username, content=content, visibility=visibility, expiry_time=expiry_time)
		statuses_db[new_status.id] = new_status
		flash('Status has been posted!', 'success')
		return redirect(url_for('profile'))
	return render_template('status.html', title='Status', form=form)

@app.route("/contacts", methods=['GET', 'POST'])
def contacts():
	form = ContactForm()
	if form.validate_on_submit():
		# Contact management logic here
		flash('Contact has been added!', 'success')
		return redirect(url_for('contacts'))
	return render_template('contacts.html', title='Contacts', form=form)

@app.route("/chat", methods=['GET', 'POST'])
def chat():
	form = MessageForm()
	if form.validate_on_submit():
		# Messaging logic here
		flash('Message has been sent!', 'success')
		return redirect(url_for('chat'))
	return render_template('chat.html', title='Chat', form=form)

@app.route("/group", methods=['GET', 'POST'])
def group():
	form = GroupForm()
	if form.validate_on_submit():
		# Group chat logic here
		flash('Group has been created!', 'success')
		return redirect(url_for('group'))
	return render_template('group.html', title='Group', form=form)

# Rest of the code...
