from models.status import Status
from utils.database import Database

db = Database()

def post_status(user_id: str, image: str, visibility: str) -> Status:
	status = Status(user_id, image, visibility)
	db.save_status(status)
	return status

def set_visibility(user_id: str, visibility: str) -> None:
	status = db.get_status(user_id)
	if status:
		status.visibility = visibility
		db.update_status(status)
