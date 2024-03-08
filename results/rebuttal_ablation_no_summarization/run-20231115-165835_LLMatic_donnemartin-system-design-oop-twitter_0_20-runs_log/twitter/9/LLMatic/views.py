from flask import render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_login import current_user, login_required, login_user
from app import app
from models import User, db
from forms import RegistrationForm, LoginForm, EditProfileForm
from utils import save_profile_picture

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data, username=form.username.data, profile_picture='', bio='', website_link='', location='', is_private=False)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Registration successful. Please login.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', form=form, messages=get_flashed_messages(with_categories=True))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.check_password(form.password.data):
			login_user(user)
			flash('Login successful.', 'success')
			return redirect(url_for('home'))
		flash('Invalid username or password', 'error')
	return render_template('login.html', form=form, messages=get_flashed_messages(with_categories=True))

@app.route('/profile/<username>', methods=['GET'])
def view_profile(username):
	user = User.query.filter_by(username=username).first()
	if user and not user.is_private:
		return render_template('profile.html', user=user)
	flash('This profile is private.', 'error')
	return redirect(url_for('home'))

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=current_user.username).first()
		if form.profile_picture.data:
			user.profile_picture = save_profile_picture(form.profile_picture.data)
		user.bio = form.bio.data
		user.website_link = form.website_link.data
		user.location = form.location.data
		user.is_private = form.is_private.data
		db.session.commit()
		flash('Profile updated successfully.', 'success')
		return redirect(url_for('view_profile', username=user.username))
	form.bio.data = current_user.bio
	form.website_link.data = current_user.website_link
	form.location.data = current_user.location
	form.is_private.data = current_user.is_private
	return render_template('edit_profile.html', form=form)
