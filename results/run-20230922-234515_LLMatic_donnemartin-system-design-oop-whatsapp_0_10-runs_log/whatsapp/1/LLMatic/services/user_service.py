from models import User
from sqlalchemy.orm import Session


def create_user(db: Session, email: str, password: str, profile_picture: str, status_message: str, privacy_settings: dict):
	user = User(email=email, password=password, profile_picture=profile_picture, status_message=status_message, privacy_settings=privacy_settings)
	db.add(user)
	db.commit()


def get_user(db: Session, user_id: int):
	return db.query(User).filter(User.id == user_id).first()
