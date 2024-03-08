from models import User, BookClub, Meeting


def test_create_bookclub():
	user = User('testuser', 'test@test.com', 'password')
	bookclub = BookClub('testclub', 'public', user)
	assert bookclub.name == 'testclub'
	assert bookclub.privacy_setting == 'public'
	assert bookclub.creator == user
	assert bookclub.members == []


def test_join_bookclub():
	user1 = User('testuser1', 'test1@test.com', 'password')
	user2 = User('testuser2', 'test2@test.com', 'password')
	bookclub = BookClub('testclub', 'public', user1)
	bookclub.add_member(user2)
	assert user2 in bookclub.members


def test_update_privacy():
	user = User('testuser', 'test@test.com', 'password')
	bookclub = BookClub('testclub', 'public', user)
	bookclub.privacy_setting = 'private'
	assert bookclub.privacy_setting == 'private'


def test_update_role():
	user1 = User('testuser1', 'test1@test.com', 'password')
	user2 = User('testuser2', 'test2@test.com', 'password')
	bookclub = BookClub('testclub', 'public', user1)
	bookclub.add_member(user2)
	bookclub.update_member_role(user2, 'admin')
	assert user2.role == 'admin'


def test_create_meeting():
	user = User('testuser', 'test@test.com', 'password')
	bookclub = BookClub('testclub', 'public', user)
	meeting = Meeting('2022-12-31', '12:00', 'Online')
	bookclub.add_meeting(meeting)
	assert meeting in bookclub.meetings


def test_update_meeting():
	user = User('testuser', 'test@test.com', 'password')
	bookclub = BookClub('testclub', 'public', user)
	meeting = Meeting('2022-12-31', '12:00', 'Online')
	bookclub.add_meeting(meeting)
	bookclub.update_meeting(meeting, '2023-01-01', '13:00', 'Offline')
	assert meeting.date == '2023-01-01'
	assert meeting.time == '13:00'
	assert meeting.location == 'Offline'


def test_delete_meeting():
	user = User('testuser', 'test@test.com', 'password')
	bookclub = BookClub('testclub', 'public', user)
	meeting = Meeting('2022-12-31', '12:00', 'Online')
	bookclub.add_meeting(meeting)
	bookclub.delete_meeting(meeting)
	assert meeting not in bookclub.meetings
