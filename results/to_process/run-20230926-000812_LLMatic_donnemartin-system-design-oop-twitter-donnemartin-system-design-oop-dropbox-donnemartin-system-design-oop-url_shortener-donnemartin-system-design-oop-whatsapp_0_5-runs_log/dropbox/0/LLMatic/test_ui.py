import pytest
from ui import UI

def test_switch_theme():
	ui = UI()
	assert ui.switch_theme('dark') == 'dark'
	assert ui.switch_theme('light') == 'light'

def test_adjust_screen_size():
	ui = UI()
	assert ui.adjust_screen_size('small') == 'small'
	assert ui.adjust_screen_size('large') == 'large'

def test_preview_file():
	ui = UI()
	assert ui.preview_file('file1') == 'Preview of file: file1'
	assert ui.preview_file('file2') == 'Preview of file: file2'

