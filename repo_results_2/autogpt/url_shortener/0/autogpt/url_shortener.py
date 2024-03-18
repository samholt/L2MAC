import json
import random
import string
import requests
from flask import Flask, redirect, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
admin = Admin(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    urls = db.relationship('URL', backref='user', lazy=True)


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(120), nullable=False)
    shortened_url = db.Column(db.String(5), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)
    click_data = db.Column(db.PickleType, default=[])
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=True)


db.create_all()
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(URL, db.session))


@app.route('/<shortened_url>')
def redirect_to_original(shortened_url):
    url = URL.query.filter_by(shortened_url=shortened_url).first()
    if url and (url.expiration_date is None or datetime.now() < url.expiration_date):
        url.clicks += 1
        url.click_data.append(str(datetime.now()))
        db.session.commit()
        return redirect(url.original_url)
    else:
        return 'URL not found or expired', 404