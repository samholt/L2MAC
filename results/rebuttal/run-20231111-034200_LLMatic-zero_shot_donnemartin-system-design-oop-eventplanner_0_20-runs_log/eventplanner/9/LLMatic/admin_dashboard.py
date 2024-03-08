from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/admin/dashboard')
def dashboard():
	# Fetch user activities
	user_activities = db.get_user_activities()
	# Fetch system performance data
	system_performance = db.get_system_performance()
	# Fetch vendor listings
	vendor_listings = db.get_vendor_listings()

	return render_template('dashboard.html', user_activities=user_activities, system_performance=system_performance, vendor_listings=vendor_listings)

if __name__ == '__main__':
	app.run(debug=True)
