from flask import Blueprint, request, jsonify
from .models import Group, User


# Create a blueprint for groups

groups = Blueprint('groups', __name__)

# Mock database
users = []
groups_db = []


@groups.route('/create', methods=['POST'])
def create_group():
	data = request.get_json()
	group_name = data.get('name')
	user_id = data.get('user_id')
	if not group_name or not user_id:
		return jsonify({'message': 'Missing parameters'}), 400
	group = Group(id=len(groups_db)+1, name=group_name, picture=None, participants=[], admins=[user_id])
	groups_db.append(group)
	return jsonify({'message': 'Group created successfully', 'group': group}), 201


@groups.route('/edit/<int:group_id>', methods=['PUT'])
def edit_group(group_id):
	data = request.get_json()
	group_name = data.get('name')
	group_picture = data.get('picture')
	group = next((g for g in groups_db if g.id == group_id), None)
	if not group:
		return jsonify({'message': 'Group not found'}), 404
	group.name = group_name
	group.picture = group_picture
	return jsonify({'message': 'Group updated successfully', 'group': group}), 200


@groups.route('/manage/<int:group_id>', methods=['POST', 'DELETE', 'PUT'])
def manage_group(group_id):
	data = request.get_json()
	user_id = data.get('user_id')
	group = next((g for g in groups_db if g.id == group_id), None)
	if not group:
		return jsonify({'message': 'Group not found'}), 404
	if request.method == 'POST':
		user = next((u for u in users if u.id == user_id), None)
		if not user:
			return jsonify({'message': 'User not found'}), 404
		group.add_participant(user)
		return jsonify({'message': 'User added to group', 'group': group}), 200
	elif request.method == 'DELETE':
		user = next((u for u in group.participants if u.id == user_id), None)
		if not user:
			return jsonify({'message': 'User not found in group'}), 404
		group.remove_participant(user)
		return jsonify({'message': 'User removed from group', 'group': group}), 200
	elif request.method == 'PUT':
		admin_id = data.get('admin_id')
		if admin_id:
			user = next((u for u in users if u.id == admin_id), None)
			if not user:
				return jsonify({'message': 'User not found'}), 404
			group.add_admin(user)
			return jsonify({'message': 'User added as admin', 'group': group}), 200
		else:
			user = next((u for u in group.admins if u.id == user_id), None)
			if not user:
				return jsonify({'message': 'User not found in group admins'}), 404
			group.remove_admin(user)
			return jsonify({'message': 'User removed from admin', 'group': group}), 200
