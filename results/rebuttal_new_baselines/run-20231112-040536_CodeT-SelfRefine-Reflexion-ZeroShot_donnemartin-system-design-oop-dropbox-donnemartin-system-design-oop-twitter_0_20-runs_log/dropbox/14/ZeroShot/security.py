activity_log = []

def log_activity(action):
	activity_log.append(action)

def get_activity_log():
	return activity_log, 200
