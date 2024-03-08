from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db
from .models import User

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def view_profile():
	user = [u for u in db if u.email == current_user.email][0]
	if not user:
		flash('User not found.')
		return redirect(url_for('main.index'))
	return render_template('profile.html', user=user)

@profile.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
	if request.method == 'POST':
		current_user.name = request.form.get('name')
		current_user.profile_picture = request.form.get('profile_picture')
		current_user.status_message = request.form.get('status_message')
		flash('Your changes have been saved.')
		return redirect(url_for('profile.view_profile'))
	else:
		return render_template('edit_profile.html', user=current_user)

@profile.route('/profile/privacy', methods=['GET', 'POST'])
@login_required
def privacy_settings():
	if request.method == 'POST':
		current_user.private_account = request.form.get('private_account')
		flash('Your changes have been saved.')
		return redirect(url_for('profile.view_profile'))
	else:
		return render_template('privacy_settings.html', user=current_user)
