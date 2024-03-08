from flask import Flask, request

app = Flask(__name__)
budget = {}

@app.route('/set_budget', methods=['POST'])
def set_budget():
	global budget
	budget = request.get_json()
	return 'Budget set', 200

@app.route('/track_budget', methods=['GET'])
def track_budget():
	global budget
	return budget, 200

@app.route('/budget_alert', methods=['GET'])
def budget_alert():
	global budget
	if budget['current'] > budget['limit']:
		return {'alert': 'Budget limit exceeded'}, 200
	else:
		return {'alert': 'Budget is under control'}, 200

if __name__ == '__main__':
	app.run(port=5003, debug=False)
