from flask import request, jsonify
from models.alert import Alert


def create_alert():
	data = request.get_json()
	alert = Alert.create_alert(data['user_id'], data['message'])
	return jsonify({'message': 'Alert created successfully'}), 201

def get_user_alerts():
	data = request.get_json()
	alerts = Alert.get_user_alerts(data['user_id'])
	return jsonify({'alerts': [alert.__dict__ for alert in alerts]}), 200

