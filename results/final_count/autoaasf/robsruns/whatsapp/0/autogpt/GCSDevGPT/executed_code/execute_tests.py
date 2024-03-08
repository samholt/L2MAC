class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        return self.username == username and self.password == password

class Status:
    def __init__(self, user, text):
        self.user = user
        self.text = text

    def post(self):
        # In a real system, this would post the status for the user
        pass

def test_status_story():
    user1 = User('user1', 'password1')
    status = Status(user1, 'Hello, world!')
    assert status.user == user1
    assert status.text == 'Hello, world!'

test_status_story()