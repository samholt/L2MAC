from task_22 import filter_integers

def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([]) == []
    assert filter_integers(['abc', {}, []]) == []
    assert filter_integers([1, 2, 3]) == [1, 2, 3]
