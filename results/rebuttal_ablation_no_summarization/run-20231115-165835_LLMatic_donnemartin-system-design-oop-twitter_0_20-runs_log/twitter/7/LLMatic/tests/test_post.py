import pytest
import post


def test_create_post():
	new_post = post.create_post('test_user', 'test_text', 'test_images')
	assert new_post.user == 'test_user'
	assert new_post.text == 'test_text'
	assert new_post.images == 'test_images'


def test_delete_post():
	new_post = post.create_post('test_user', 'test_text', 'test_images')
	post_id = list(post.posts_db.keys())[-1]
	assert post.delete_post(post_id) == True
	assert post_id not in post.posts_db


def test_search():
	new_post = post.create_post('testuser', 'test_text', 'test_images')
	results = post.search('test')
	assert 'testuser' in [post.user for post in results['posts']]
	assert new_post in results['posts']


def test_filter():
	new_post = post.create_post('test_user', '#test', 'test_images')
	results = post.filter('#test')
	assert new_post in results


def test_get_trending_topics():
	new_post1 = post.create_post('test_user', '#test1', 'test_images')
	new_post2 = post.create_post('test_user', '#test2', 'test_images')
	new_post3 = post.create_post('test_user', '#test1', 'test_images')
	results = post.get_trending_topics()
	assert results['#test1'] == 2
	assert results['#test2'] == 1


def test_get_user_recommendations():
	new_user1 = post.auth.register_user('test1@test.com', 'test_user1', 'test_password')
	new_user2 = post.auth.register_user('test2@test.com', 'test_user2', 'test_password')
	new_user3 = post.auth.register_user('test3@test.com', 'test_user3', 'test_password')
	post.auth.follow_user('test_user2', 'test_user1')
	post.auth.follow_user('test_user3', 'test_user1')
	results = post.get_user_recommendations('test_user2')
	assert 'test_user1' in results

