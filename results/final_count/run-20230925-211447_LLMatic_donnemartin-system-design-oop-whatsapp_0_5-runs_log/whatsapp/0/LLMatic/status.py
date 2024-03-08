import uuid

# Mock database
statuses = {}


def post_status(email, image, visibility):
	"""Post a new status."""
	status_id = str(uuid.uuid4())
	statuses[status_id] = {
		'email': email,
		'image': image,
		'visibility': visibility,
	}
	return status_id


def update_visibility(email, status_id, visibility_emails):
	"""Update the visibility of a status."""
	if status_id in statuses and statuses[status_id]['email'] == email:
		statuses[status_id]['visibility'] = visibility_emails
		return True
	return False
