from dataclasses import dataclass

@dataclass
class Activity:
	user_email: str
	action: str
	timestamp: str

activities = {}


def get_activity(data):
	activity = activities.get(data['user_email'])
	if activity:
		return {'status': 'success', 'activity': activity}
	else:
		return {'status': 'error', 'message': 'No activity found'}
