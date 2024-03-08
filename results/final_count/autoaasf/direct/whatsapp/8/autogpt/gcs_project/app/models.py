from gcs_project.app import db, login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True)

    @property
    def is_active(self):
        return self.active


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))