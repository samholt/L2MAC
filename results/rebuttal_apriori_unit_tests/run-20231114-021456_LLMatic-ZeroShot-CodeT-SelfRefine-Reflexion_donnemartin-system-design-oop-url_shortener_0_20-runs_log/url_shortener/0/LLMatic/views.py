from flask import Blueprint, redirect, request
from models import URL, User, Admin

bp = Blueprint('views', __name__)

@bp.route('/<string:short_url>')
def redirect_to_url(short_url):
	url = URL.find_by_short_url(short_url)
	if url:
		return redirect(url.original_url, code=302)
	else:
		return 'URL not found', 404

@bp.route('/create_account', methods=['POST'])
def create_account():
	username = request.form['username']
	password = request.form['password']
	user = User(username, password)
	User.save_to_db(user)
	return 'Account created successfully', 200

@bp.route('/<string:username>/urls')
def get_user_urls(username):
	user = User.find_by_username(username)
	if user:
		return {'urls': [url.shortened_url for url in user.urls]}
	else:
		return 'User not found', 404

@bp.route('/<string:username>/edit_url', methods=['POST'])
def edit_user_url(username):
	user = User.find_by_username(username)
	if user:
		old_url = request.form['old_url']
		new_url = request.form['new_url']
		if user.edit_url(old_url, new_url):
			return 'URL edited successfully', 200
		else:
			return 'URL not found', 404
	else:
		return 'User not found', 404

@bp.route('/<string:username>/delete_url', methods=['POST'])
def delete_user_url(username):
	user = User.find_by_username(username)
	if user:
		url = request.form['url']
		if user.delete_url(url):
			return 'URL deleted successfully', 200
		else:
			return 'URL not found', 404
	else:
		return 'User not found', 404

@bp.route('/<string:username>/analytics', methods=['POST'])
def get_user_analytics(username):
	user = User.find_by_username(username)
	if user:
		url = request.form['url']
		analytics = user.get_analytics(url)
		if analytics is not None:
			return {'analytics': analytics}
		else:
			return 'URL not found', 404
	else:
		return 'User not found', 404

@bp.route('/admin/<string:username>/all_urls')
def get_all_urls(username):
	admin = Admin.find_by_username(username)
	if admin:
		return {'urls': [url.shortened_url for url in admin.get_all_urls()]}
	else:
		return 'Admin not found', 404

@bp.route('/admin/<string:username>/delete_url', methods=['POST'])
def delete_url(username):
	admin = Admin.find_by_username(username)
	if admin:
		url = request.form['url']
		if admin.delete_url(url):
			return 'URL deleted successfully', 200
		else:
			return 'URL not found', 404
	else:
		return 'Admin not found', 404

@bp.route('/admin/<string:username>/delete_user', methods=['POST'])
def delete_user(username):
	admin = Admin.find_by_username(username)
	if admin:
		user_to_delete = request.form['user']
		if admin.delete_user(user_to_delete):
			return 'User deleted successfully', 200
		else:
			return 'User not found', 404
	else:
		return 'Admin not found', 404

@bp.route('/admin/<string:username>/system_stats')
def get_system_stats(username):
	admin = Admin.find_by_username(username)
	if admin:
		return {'system_stats': admin.get_system_stats()}
	else:
		return 'Admin not found', 404
