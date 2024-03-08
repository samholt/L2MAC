from ui import UI

def test_switch_theme():
	ui = UI()
	ui.switch_theme('dark')
	assert ui.theme == 'dark'


def test_adjust_for_device():
	ui = UI()
	ui.adjust_for_device('mobile')
	assert ui.device == 'mobile'


def test_generate_file_preview():
	ui = UI()
	result = ui.generate_file_preview('test_file')
	assert result == 'File preview for: test_file'

