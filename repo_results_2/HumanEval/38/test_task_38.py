from task_38 import encode_cyclic, decode_cyclic

def test_encode_cyclic():
	assert encode_cyclic('abc') == 'bca'
	assert encode_cyclic('abcdef') == 'bcaefd'
	assert encode_cyclic('abcdefg') == 'bcaefdg'
	assert encode_cyclic('abcdefgh') == 'bcaefdgh'

def test_decode_cyclic():
	assert decode_cyclic('bca') == 'abc'
	assert decode_cyclic('bcaefd') == 'abcdef'
	assert decode_cyclic('bcaefdg') == 'abcdefg'
	assert decode_cyclic('bcaefdgh') == 'abcdefgh'
