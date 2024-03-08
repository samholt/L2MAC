from flask import Flask, request
from events import Event
from venues import Venue
from guests import Guest
from vendors import Vendor
from budget import Budget
from users import User
from notifications import Notification
from reports import Report
from admin import Admin
from security import Security

app = Flask(__name__)
event_manager = Event()
venue_manager = Venue()
guest_manager = Guest()
vendor_manager = Vendor()
budget_manager = Budget()
user_manager = User()
notification_manager = Notification()
report_manager = Report()
admin_manager = Admin()
security_manager = Security()

@app.route('/')
def home():
	return 'Hello, World!', 200

@app.route('/security/protect', methods=['POST'])
def protect_user_data():
	user_data = request.get_json()
	return security_manager.protect_user_data(user_data['user_id'], user_data), 200

@app.route('/security/privacy/<user_id>', methods=['GET'])
def ensure_privacy(user_id):
	return security_manager.ensure_privacy(user_id), 200

@app.route('/security/payment', methods=['POST'])
def secure_payment_gateway():
	payment_data = request.get_json()
	return security_manager.secure_payment_gateway(payment_data['user_id'], payment_data), 200

# Rest of the code...
