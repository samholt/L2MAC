import pygame
import pytest
from main import Food, Snake

# Mock pygame to run headless
pygame.display.set_mode = lambda x: None
pygame.init = lambda: None
pygame.quit = lambda: None


@pytest.fixture
def snake():
    return Snake()


@pytest.fixture
def food():
    return Food()


@pytest.mark.parametrize(
    "direction, expected_position",
    [("up", (400, 290)), ("down", (400, 310)), ("left", (390, 300)), ("right", (410, 300))],
)
def test_snake_movement(snake, direction, expected_position):
    snake.direction = direction
    snake.move()
    assert snake.positions[0] == expected_position


@pytest.mark.parametrize("initial_score, expected_score", [(0, 1), (5, 6)])
def test_snake_eating(snake, food, initial_score, expected_score):
    snake.score = initial_score
    snake.positions[0] = food.position  # Simulate snake eating the food
    snake.grow()
    assert snake.score == expected_score


@pytest.mark.parametrize("initial_length, expected_length", [(1, 2), (3, 4)])
def test_snake_growing(snake, initial_length, expected_length):
    snake.length = initial_length
    snake.grow()
    assert snake.length == expected_length
