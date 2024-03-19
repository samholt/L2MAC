import pytest
from task_115 import max_fill

@pytest.mark.parametrize('grid, capacity, expected', [
    ([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1, 6),
    ([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2, 5),
    ([[0,0,0], [0,0,0]], 5, 0),
    ([[1,1,1], [1,1,1]], 1, 6),
    ([[1,1,1,1,1,1,1,1,1,1]], 10, 1),
    ([[1,1,1,1,1,1,1,1,1,1]], 1, 10),
    ([[1,1,1,1,1,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0]], 5, 2)
])
def test_max_fill(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected
