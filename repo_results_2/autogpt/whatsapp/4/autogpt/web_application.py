from flask import Flask, render_template, request
from user_auth import User
from user_profile import UserProfile
from contact_management import ContactManagement
from messaging_module import MessagingModule
from group_chat_module import GroupChat
from status_story_module import StatusStoryModule

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    user = User(email, password)
    return render_template('profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)