import time
import task_135

def test_can_arrange():
	assert task_135.can_arrange([1,2,4,3,5]) == 3
	assert task_135.can_arrange([1,2,3]) == -1


def test_can_arrange_large_input():
	start_time = time.time()
	input_list = list(range(1, 1000000)) + [999998]
	assert task_135.can_arrange(input_list) == 999999
	end_time = time.time()
	execution_time = end_time - start_time
	assert execution_time < 1, f'Execution time {execution_time} is too long'

