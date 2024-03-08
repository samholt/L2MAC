from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, UrlForm
from app.models import User, Url, Click
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from geopy.geocoders import Nominatim
import string
import random

@app.route('/', methods=['GET', 'POST'])
def home():
	form = UrlForm()
	if form.validate_on_submit():
		original_url = form.original_url.data
		short_url = form.short_url.data
		if not short_url:
			short_url = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
		new_url = Url(original_url=original_url, short_url=short_url, owner=current_user)
		db.session.add(new_url)
		db.session.commit()
		flash('Your URL has been shortened!', 'success')
		return redirect(url_for('home'))
	return render_template('home.html', title='Home', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data)
		user = User(username=form.username.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and check_password_hash(user.password, form.password.data):
			login_user(user)
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = Url.query.filter_by(short_url=short_url).first_or_404()
	url.clicks += 1
	db.session.commit()
	geolocator = Nominatim(user_agent='url_shortener')
	location = geolocator.geocode(request.remote_addr)
	click = Click(location=location, url=url)
	db.session.add(click)
	db.session.commit()
	return redirect(url.original_url)

@app.route('/dashboard')
@login_required
def dashboard():
	urls = Url.query.filter_by(owner=current_user)
	return render_template('dashboard.html', title='Dashboard', urls=urls)
