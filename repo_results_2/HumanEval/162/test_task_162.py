import pytest
from task_162 import string_to_md5

def test_string_to_md5():
	assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
	assert string_to_md5('') is None
	assert string_to_md5('1234567890') == 'e807f1fcf82d132f9bb018ca6738a19f'
	assert string_to_md5('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'
	assert string_to_md5('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') == 'd174ab98d277d9f5a5611c2c9f419d9f'
	assert string_to_md5('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~') == '442e9d62bc3a517609fb3b8bc29e7dd5'
	assert string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'
	assert string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
