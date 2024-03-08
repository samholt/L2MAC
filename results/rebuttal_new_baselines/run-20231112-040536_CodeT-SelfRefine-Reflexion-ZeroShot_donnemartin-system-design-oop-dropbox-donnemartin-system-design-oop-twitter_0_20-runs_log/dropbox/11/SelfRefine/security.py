activity_log = []

def log_activity(activity):
	activity_log.append(activity)
	return {'message': 'Activity logged successfully'}, 201

def get_activity_log():
	return activity_log, 200
