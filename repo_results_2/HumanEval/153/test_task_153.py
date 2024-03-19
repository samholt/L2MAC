from task_153 import Strongest_Extension

def test_Strongest_Extension():
	assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
	assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
	assert Strongest_Extension('test', ['abc', 'DEF', 'Ghi']) == 'test.DEF'
	assert Strongest_Extension('test', ['abc', 'DEF', 'GHI']) == 'test.DEF'
