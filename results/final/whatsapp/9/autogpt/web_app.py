from flask import Flask, request, jsonify
from user_auth import UserManager
from user_profiles import ProfileManager
from contact_management import ContactManager
from messaging import MessageManager
from group_chats import GroupChatManager
from status_story import StatusStoryManager

app = Flask(__name__)

user_manager = UserManager()
profile_manager = ProfileManager()
contact_manager = ContactManager()
message_manager = MessageManager()
group_chat_manager = GroupChatManager()
status_story_manager = StatusStoryManager()


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if user_manager.register_user(username, password):
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Username already exists'})


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if user_manager.authenticate_user(username, password):
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid username or password'})


if __name__ == '__main__':
    app.run(debug=True)