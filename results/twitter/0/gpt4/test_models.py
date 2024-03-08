from models import User, Tweet, DirectMessage, Mention


def test_user():
	alice = User(id=1, username='Alice', followers=[], following=[], tweets=[], direct_messages=[])
	bob = User(id=2, username='Bob', followers=[], following=[], tweets=[], direct_messages=[])

	assert alice.username == 'Alice'
	assert bob.username == 'Bob'

	alice.follow(bob)
	assert bob in alice.following
	assert alice in bob.followers


def test_tweet():
	alice = User(id=1, username='Alice', followers=[], following=[], tweets=[], direct_messages=[])
	tweet = Tweet(id=1, user=alice, content='Hello, world!', privacy='public', replies=[], mentions=[])

	assert tweet.content == 'Hello, world!'
	assert tweet.privacy == 'public'


def test_direct_message():
	alice = User(id=1, username='Alice', followers=[], following=[], tweets=[], direct_messages=[])
	bob = User(id=2, username='Bob', followers=[], following=[], tweets=[], direct_messages=[])
	dm = DirectMessage(id=1, sender=alice, receiver=bob, message='Hi Bob!')

	assert dm.message == 'Hi Bob!'
	assert dm.sender == alice
	assert dm.receiver == bob


def test_mention():
	alice = User(id=1, username='Alice', followers=[], following=[], tweets=[], direct_messages=[])
	bob = User(id=2, username='Bob', followers=[], following=[], tweets=[], direct_messages=[])
	tweet = Tweet(id=1, user=alice, content='Hello, world!', privacy='public', replies=[], mentions=[])
	mention = Mention(id=1, user=bob, tweet=tweet)

	assert mention.user == bob
	assert mention.tweet == tweet
