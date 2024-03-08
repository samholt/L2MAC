from flask import render_template, url_for, flash, redirect, request, abort
from app import app, db
from app.forms import RegistrationForm, LoginForm, UrlForm
from app.models import User, Url, Click
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from geopy.geocoders import Nominatim
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def home():
	form = UrlForm()
	if form.validate_on_submit():
		original_url = form.original_url.data
		short_url = form.short_url.data
		if not short_url:
			short_url = generate_short_url()
		new_url = Url(original_url=original_url, short_url=short_url, creator=current_user)
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
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
	return render_template('account.html', title='Account')

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = Url.query.filter_by(short_url=short_url).first_or_404()
	url.clicks += 1
	click = Click(url=url, location=get_location())
	db.session.add(click)
	db.session.commit()
	return redirect(url.original_url)

@app.route('/analytics/<short_url>')
@login_required
def analytics(short_url):
	url = Url.query.filter_by(short_url=short_url).first_or_404()
	if url.creator != current_user:
		abort(403)
	clicks = Click.query.filter_by(url=url).all()
	return render_template('analytics.html', title='Analytics', url=url, clicks=clicks)

@app.route('/delete/<short_url>', methods=['POST'])
@login_required
def delete_url(short_url):
	url = Url.query.filter_by(short_url=short_url).first_or_404()
	if url.creator != current_user:
		abort(403)
	db.session.delete(url)
	db.session.commit()
	flash('Your URL has been deleted!', 'success')
	return redirect(url_for('account'))

@app.route('/admin')
@login_required
def admin():
	if not current_user.is_admin:
		abort(403)
	users = User.query.all()
	urls = Url.query.all()
	return render_template('admin.html', title='Admin', users=users, urls=urls)

@app.route('/delete_user/<user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
	if not current_user.is_admin:
		abort(403)
	user = User.query.get(user_id)
	if not user:
		abort(404)
	db.session.delete(user)
	db.session.commit()
	flash('The user has been deleted!', 'success')
	return redirect(url_for('admin'))

@app.route('/delete_all_urls', methods=['POST'])
@login_required
def delete_all_urls():
	if not current_user.is_admin:
		abort(403)
	urls = Url.query.all()
	for url in urls:
		db.session.delete(url)
	db.session.commit()
	flash('All URLs have been deleted!', 'success')
	return redirect(url_for('admin'))

@app.route('/delete_all_users', methods=['POST'])
@login_required
def delete_all_users():
	if not current_user.is_admin:
		abort(403)
	users = User.query.all()
	for user in users:
		db.session.delete(user)
	db.session.commit()
	flash('All users have been deleted!', 'success')
	return redirect(url_for('admin'))

def generate_short_url():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def get_location():
	geolocator = Nominatim(user_agent='url_shortener')
	location = geolocator.geocode(request.remote_addr)
	return location.address if location else 'Unknown'
