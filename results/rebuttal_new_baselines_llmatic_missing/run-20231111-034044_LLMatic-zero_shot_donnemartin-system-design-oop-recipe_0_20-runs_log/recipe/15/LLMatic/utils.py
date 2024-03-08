def validate_user_input(input_data):
	if not isinstance(input_data, dict):
		return False
	required_fields = ['name', 'email']
	for field in required_fields:
		if field not in input_data:
			return False
	return True

def handle_error(error):
	return {'status': 'error', 'message': str(error)}

def format_response(data):
	return {'status': 'success', 'data': data}
