from flask import Flask
from models import User, Comment, Message, Notification, TrendingTopic
from services import UserService, PostService, SocialInteractionService, TrendingDiscoveryService
import routes

app = Flask(__name__)

if __name__ == '__main__':
	app.run(debug=True)
