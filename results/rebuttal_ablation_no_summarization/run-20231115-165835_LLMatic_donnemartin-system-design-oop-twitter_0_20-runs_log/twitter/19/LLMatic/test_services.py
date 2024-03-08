from services import register_user, authenticate_user, edit_profile, toggle_privacy, create_post, delete_post, search_posts


def test_register_user():
	assert register_user('test1@test.com', 'testuser', 'testpass') == True
	assert register_user('test2@test.com', 'testuser2', 'testpass2') == True

def test_authenticate_user():
	assert authenticate_user('test1@test.com', 'testpass') == True
	assert authenticate_user('test1@test.com', 'wrongpass') == False
	assert authenticate_user('notexist@test.com', 'testpass') == False

def test_edit_profile():
	assert edit_profile('test1@test.com', 'newpic.jpg', 'newbio', 'newwebsite.com', 'newlocation') == True
	assert edit_profile('notexist@test.com', 'newpic.jpg', 'newbio', 'newwebsite.com', 'newlocation') == False

def test_toggle_privacy():
	assert toggle_privacy('test1@test.com') == True
	assert toggle_privacy('notexist@test.com') == False

def test_create_post():
	assert create_post('test1@test.com', 'Hello, world!', ['pic1.jpg', 'pic2.jpg']) == True
	assert create_post('notexist@test.com', 'Hello, world!', ['pic1.jpg', 'pic2.jpg']) == False

def test_delete_post():
	assert delete_post(0) == True
	assert delete_post(100) == False

def test_search_posts():
	assert 'Hello, world!' in [post.text_content for post in search_posts('Hello')]
	assert 'Hello, world!' not in [post.text_content for post in search_posts('Goodbye')]
