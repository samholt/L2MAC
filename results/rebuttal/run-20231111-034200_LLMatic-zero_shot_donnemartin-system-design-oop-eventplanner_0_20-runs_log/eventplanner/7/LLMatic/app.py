from flask import Flask, request
import budget_management
import user_accounts
import reporting
import admin_dashboard

app = Flask(__name__)

@app.route('/set_budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	budget_management.set_budget(**data)
	return 'Budget set successfully', 200

@app.route('/track_budget', methods=['GET'])
def track_budget():
	return budget_management.track_budget(), 200

@app.route('/budget_alert', methods=['GET'])
def budget_alert():
	return budget_management.budget_alert(), 200

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user_accounts.create_user(**data)
	return 'User created successfully', 200

@app.route('/get_user', methods=['GET'])
def get_user():
	username = request.args.get('username')
	user = user_accounts.get_user(username)
	if user:
		return user.__dict__, 200
	else:
		return 'User not found', 404

@app.route('/generate_report', methods=['GET'])
def generate_report():
	event_id = request.args.get('event_id')
	return reporting.generate_report(event_id), 200

@app.route('/collect_feedback', methods=['POST'])
def collect_feedback():
	data = request.get_json()
	reporting.collect_feedback(**data)
	return 'Feedback collected', 200

@app.route('/monitor_user_activities', methods=['GET'])
def monitor_user_activities():
	user_id = request.args.get('user_id')
	return admin_dashboard.monitor_user_activities(user_id), 200

@app.route('/system_performance_analytics', methods=['GET'])
def system_performance_analytics():
	return admin_dashboard.system_performance_analytics(), 200

@app.route('/manage_vendor_listings', methods=['POST'])
def manage_vendor_listings():
	data = request.get_json()
	return admin_dashboard.manage_vendor_listings(**data), 200

@app.route('/manage_platform_content', methods=['POST'])
def manage_platform_content():
	data = request.get_json()
	return admin_dashboard.manage_platform_content(**data), 200

if __name__ == '__main__':
	app.run(port=5002, debug=False)
