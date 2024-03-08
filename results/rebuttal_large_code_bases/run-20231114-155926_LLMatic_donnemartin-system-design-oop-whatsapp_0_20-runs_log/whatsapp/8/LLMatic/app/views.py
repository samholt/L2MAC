from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import create_app, socketio
from app.database import MockDatabase as db
from app.models import User, Message, Group, Status
from app.forms import LoginForm, RegistrationForm, ResetPasswordForm, SendMessageForm, PostStatusForm

app, socketio = create_app('default')

@app.route('/')
@app.route('/index')
@login_required
def index():
    pass
