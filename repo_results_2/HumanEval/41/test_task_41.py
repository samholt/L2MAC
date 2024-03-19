import pytest
from task_41 import car_race_collision

def test_car_race_collision():
	assert car_race_collision(5) == 5
	assert car_race_collision(10) == 10
	assert car_race_collision(0) == 0
