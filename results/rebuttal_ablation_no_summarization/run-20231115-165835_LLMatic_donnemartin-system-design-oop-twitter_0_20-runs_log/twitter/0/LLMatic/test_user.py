import user
import post
import pytest

def sort_users(user1, users):
	# Sort users based on the number of posts and mutual followers with user1
	return sorted(users, key=lambda user: (len(user.posts), len(set(user1.following).intersection(user.following))), reverse=True)

def test_recommend_users():
	# Create users
	user1 = user.User('email1', 'user1', 'password1', False)
	user2 = user.User('email2', 'user2', 'password2', False)
	user3 = user.User('email3', 'user3', 'password3', False)
	user4 = user.User('email4', 'user4', 'password4', False)
	user5 = user.User('email5', 'user5', 'password5', False)
	user6 = user.User('email6', 'user6', 'password6', False)
	user7 = user.User('email7', 'user7', 'password7', False)
	# Add users to the database
	user.users_db['user1'] = user1
	user.users_db['user2'] = user2
	user.users_db['user3'] = user3
	user.users_db['user4'] = user4
	user.users_db['user5'] = user5
	user.users_db['user6'] = user6
	user.users_db['user7'] = user7
	# Create posts with hashtags
	post1 = post.Post(user1, 'text #hashtag1', 'image1', 'timestamp1')
	post2 = post.Post(user2, 'text #hashtag1', 'image2', 'timestamp2')
	post3 = post.Post(user3, 'text #hashtag2', 'image3', 'timestamp3')
	post4 = post.Post(user4, 'text #hashtag1', 'image4', 'timestamp4')
	post5 = post.Post(user5, 'text #hashtag3', 'image5', 'timestamp5')
	post6 = post.Post(user6, 'text #hashtag1', 'image6', 'timestamp6')
	post7 = post.Post(user7, 'text #hashtag1', 'image7', 'timestamp7')
	# Add posts to the users
	user1.posts.append(post1)
	user2.posts.append(post2)
	user3.posts.append(post3)
	user4.posts.append(post4)
	user5.posts.append(post5)
	user6.posts.append(post6)
	user7.posts.append(post7)
	# User1 follows user2 and user3
	user1.follow(user2)
	user1.follow(user3)
	# User4 and User7 follow user1
	user4.follow(user1)
	user7.follow(user1)
	# Recommend users for user1
	recommendations = user1.recommend_users()
	# Check if the recommendations are correct
	user1_hashtags = set(hashtag for post in user1.posts for hashtag in post.text.split() if hashtag.startswith('#'))
	expected_users = sort_users(user1, [user for user in user.users_db.values() if user != user1 and any(hashtag in post.text.split() for post in user.posts for hashtag in post.text.split() if hashtag.startswith('#') and hashtag in user1_hashtags)])
	assert len(recommendations) == len(expected_users[:5])
	assert set(user.username for user in recommendations) == set(user.username for user in expected_users[:5])

pytest.main(['-v'])

