from flask import Flask, request
from models import db, User, BookClub, BookClubMembership, Meeting, Discussion, Comment, Vote
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	club = BookClub(name=data['club_name'], creator=user)
	db.session.add(club)
	db.session.commit()
	return {'message': 'Book club created successfully'}, 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	club = BookClub.query.get(data['club_id'])
	membership = BookClubMembership(user_id=user.id, bookclub_id=club.id)
	db.session.add(membership)
	db.session.commit()
	return {'message': 'Joined book club successfully'}, 200

@app.route('/set_privacy', methods=['POST'])
def set_privacy():
	data = request.get_json()
	club = BookClub.query.get(data['club_id'])
	if club.creator_id == data['user_id']:
		club.privacy = data['privacy']
		db.session.commit()
		return {'message': 'Privacy setting updated successfully'}, 200
	else:
		return {'message': 'Only the club creator can change the privacy setting'}, 403

@app.route('/assign_role', methods=['POST'])
def assign_role():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	club = BookClub.query.get(data['club_id'])
	membership = BookClubMembership.query.filter_by(user_id=user.id, bookclub_id=club.id).first()
	if membership and club.creator_id == data['admin_id']:
		membership.role = data['role']
		db.session.commit()
		return {'message': 'Role assigned successfully'}, 200
	else:
		return {'message': 'Only the club creator can assign roles'}, 403

@app.route('/set_permissions', methods=['POST'])
def set_permissions():
	data = request.get_json()
	club = BookClub.query.get(data['club_id'])
	if club.creator_id == data['admin_id']:
		club.permissions = data['permissions']
		db.session.commit()
		return {'message': 'Permissions set successfully'}, 200
	else:
		return {'message': 'Only the club creator can set permissions'}, 403

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	club = BookClub.query.get(data['club_id'])
	if club.creator_id == data['user_id']:
		meeting_date = datetime.strptime(data['date'], '%Y-%m-%d')
		meeting_time = datetime.strptime(data['time'], '%H:%M:%S').time()
		meeting = Meeting(date=meeting_date, time=meeting_time, location=data['location'], club_id=club.id)
		db.session.add(meeting)
		db.session.commit()
		return {'message': 'Meeting scheduled successfully'}, 200
	else:
		return {'message': 'Only the club creator can schedule meetings'}, 403

@app.route('/send_reminders', methods=['GET'])
def send_reminders():
	data = request.get_json()
	club = BookClub.query.get(data['club_id'])
	if club.creator_id == data['user_id']:
		# In a real-world application, here we would send an email or notification to all members of the club
		# For this task, we will just return a success message
		return {'message': 'Reminders sent successfully'}, 200
	else:
		return {'message': 'Only the club creator can send reminders'}, 403

@app.route('/create_discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	club = BookClub.query.get(data['club_id'])
	discussion = Discussion(title=data['title'], content=data['content'], club_id=club.id, user_id=user.id)
	db.session.add(discussion)
	db.session.commit()
	return {'message': 'Discussion created successfully'}, 201

@app.route('/create_comment', methods=['POST'])
def create_comment():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	discussion = Discussion.query.get(data['discussion_id'])
	comment = Comment(content=data['content'], discussion_id=discussion.id, user_id=user.id)
	db.session.add(comment)
	db.session.commit()
	return {'message': 'Comment created successfully'}, 201

@app.route('/vote', methods=['POST'])
def vote():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	club = BookClub.query.get(data['club_id'])
	vote = Vote(book_id=data['book_id'], club_id=club.id, user_id=user.id)
	db.session.add(vote)
	db.session.commit()
	return {'message': 'Vote cast successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
