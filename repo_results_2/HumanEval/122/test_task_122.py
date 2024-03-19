import pytest
from task_122 import add_elements

@pytest.mark.parametrize('arr, k, expected', [
    ([111,21,3,4000,5,6,7,8,9], 4, 24),
    ([1,2,3,4,5,6,7,8,9], 5, 15),
    ([10,20,30,40,50], 5, 150),
    ([100,200,300,400,500], 5, 0),
    ([-1,-2,-3,-4,-5], 5, -15),
])
def test_add_elements(arr, k, expected):
    assert add_elements(arr, k) == expected

if __name__ == '__main__':
    pytest.main([__file__])
