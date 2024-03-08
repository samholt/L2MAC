from flask import Blueprint, request
from flask_login import login_required, current_user
from group import Group
from app import db

group_blueprint = Blueprint('group', __name__)

@group_blueprint.route('/create', methods=['POST'])
@login_required
def create_group():
    data = request.get_json()
    new_group = Group(name=data['name'], creator_id=current_user.id)
    db.session.add(new_group)
    db.session.commit()
    return 'New group created!', 201
