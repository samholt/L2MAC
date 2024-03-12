from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	profile_picture = db.Column(db.String(200), nullable=True)
	bio = db.Column(db.String(500), nullable=True)
	website_link = db.Column(db.String(200), nullable=True)
	location = db.Column(db.String(100), nullable=True)
	is_private = db.Column(db.Boolean, default=False)
	followed = db.relationship('User', secondary=followers, primaryjoin=(followers.c.follower_id == id), secondaryjoin=(followers.c.followed_id == id), backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def follow(self, user):
		if not self.is_following(user):
			self.followed.append(user)
			db.session.commit()

	def unfollow(self, user):
		if self.is_following(user):
			self.followed.remove(user)
			db.session.commit()

	def is_following(self, user):
		return self.followed.filter(followers.c.followed_id == user.id).count() > 0

	@classmethod
	def search(cls, keyword):
		return cls.query.filter(cls.username.contains(keyword)).all()

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(500), nullable=False)
	images = db.Column(db.String(500), nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('posts', lazy=True))
	likes = db.Column(db.Integer, default=0)
	retweets = db.Column(db.Integer, default=0)
	replies = db.relationship('Reply', backref='post', lazy=True)

	@classmethod
	def search(cls, keyword):
		return cls.query.filter(cls.content.contains(keyword)).all()

	@classmethod
	def filter(cls, filter_type, keyword):
		if filter_type == 'hashtags':
			return cls.query.filter(cls.content.contains('#' + keyword)).all()
		elif filter_type == 'mentions':
			return cls.query.filter(cls.content.contains('@' + keyword)).all()
		elif filter_type == 'trending':
			# For simplicity, we consider a post as trending if it has more than 100 likes or retweets
			return cls.query.filter((cls.likes > 100) | (cls.retweets > 100)).all()
		else:
			return []

class Reply(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(500), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
