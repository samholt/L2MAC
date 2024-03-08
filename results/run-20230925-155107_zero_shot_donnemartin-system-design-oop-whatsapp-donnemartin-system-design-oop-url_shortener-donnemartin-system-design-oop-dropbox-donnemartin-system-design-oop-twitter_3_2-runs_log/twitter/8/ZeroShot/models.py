from app import db, ma
from flask_jwt_extended import get_jwt_identity
from sqlalchemy.orm import backref


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	profile_picture = db.Column(db.String(120), nullable=True)
	bio = db.Column(db.String(280), nullable=True)
	website = db.Column(db.String(120), nullable=True)
	location = db.Column(db.String(120), nullable=True)
	is_private = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '<User %r>' % self.username


class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User
		load_instance = True
