from flask import Flask, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/budget', methods=['POST'])
def set_budget():
	budget = request.get_json()
	return {'id': db.insert('budget', budget)}, 201

@app.route('/budget/<int:id>', methods=['GET'])
def get_budget(id):
	return db.get('budget', id)

@app.route('/budget/<int:id>', methods=['PUT'])
def update_budget(id):
	budget = request.get_json()
	if db.update('budget', id, budget):
		return db.get('budget', id)
	else:
		return {'error': 'Budget not found'}, 404

@app.route('/budget/<int:id>/overrun', methods=['GET'])
def check_budget_overrun(id):
	budget = db.get('budget', id)
	if not budget:
		return {'error': 'Budget not found'}, 404
	if budget['spent'] > budget['total']:
		return {'overrun': True}
	else:
		return {'overrun': False}
