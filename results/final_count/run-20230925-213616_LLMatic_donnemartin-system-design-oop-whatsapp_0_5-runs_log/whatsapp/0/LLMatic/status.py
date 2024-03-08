import dataclasses

@dataclasses.dataclass
class Status:
	email: str
	content: str
	visibility: str
	is_online: bool = False


status_dict = {}


def post_status(email: str, content: str, visibility: str):
	status = Status(email, content, visibility)
	status_dict[email] = status
	return status


def set_online_status(email: str, is_online: bool):
	status = status_dict.get(email)
	if status:
		status.is_online = is_online
