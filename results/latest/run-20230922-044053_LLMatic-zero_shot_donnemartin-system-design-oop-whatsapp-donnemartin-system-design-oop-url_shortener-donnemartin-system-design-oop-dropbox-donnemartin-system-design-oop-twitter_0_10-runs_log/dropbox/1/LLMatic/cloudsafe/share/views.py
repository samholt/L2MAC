from flask import request, jsonify
from .models import Share


def generate_shareable_link():
    data = request.get_json()
    share = Share(**data)
    link = share.generate_shareable_link()
    return jsonify({'link': link}), 200


def manage_shared_folder():
    data = request.get_json()
    share = Share(**data)
    share.manage_shared_folder()
    return jsonify({'message': 'Shared folder managed successfully'}), 200
