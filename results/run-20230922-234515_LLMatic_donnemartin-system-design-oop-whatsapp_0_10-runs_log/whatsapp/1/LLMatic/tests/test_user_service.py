from services.user_service import create_user, get_user
from models import User
from sqlalchemy.orm import Session


def test_create_user(db: Session):
	create_user(db, 'test@test.com', 'password', 'profile_picture.jpg', 'Hello, world!', {'last_seen': False})
	user = db.query(User).filter(User.email == 'test@test.com').first()
	assert user is not None


def test_get_user(db: Session):
	user = get_user(db, 1)
	assert user is not None
