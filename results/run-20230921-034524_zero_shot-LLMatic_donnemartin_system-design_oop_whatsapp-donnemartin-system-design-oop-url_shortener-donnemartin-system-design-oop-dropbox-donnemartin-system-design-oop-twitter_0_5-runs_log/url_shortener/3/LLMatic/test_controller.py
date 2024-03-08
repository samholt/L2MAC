import pytest
from unittest.mock import MagicMock
from controller import Controller


def test_controller():
	controller = Controller()
	controller.view.get_long_url = MagicMock(return_value='long_url')
	controller.view.get_custom_url = MagicMock(return_value='custom_url')
	controller.view.display_short_url = MagicMock()
	controller.view.display_click_stats = MagicMock()
	controller.create_short_url()
	controller.view.display_short_url.assert_called_with('short_url')
	controller.redirect_to_long_url('short_url')
	url = controller.model.get_url('short_url')
	assert url.click_count == 1
	controller.display_click_stats('short_url')
	controller.view.display_click_stats.assert_called_with(1)
	controller.delete_expired_urls()
	assert controller.model.get_url('short_url') == url

