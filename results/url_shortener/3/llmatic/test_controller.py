import pytest
from unittest.mock import Mock
from datetime import datetime, timedelta
from controller import Controller


def test_controller():
	model = Mock()
	view = Mock()
	view.input_url.return_value = ('https://example.com', datetime.now() + timedelta(days=1))
	controller = Controller(model, view)
	controller.shorten_url()
	view.input_url.assert_called_once()
	model.generate_short_url.assert_called_once()
	view.display_short_url.assert_called_once()
	controller.redirect_url('ABCDE')
	model.get_original_url.assert_called_once()
	model.track_click.assert_called_once()
	view.redirect.assert_called_once()
	controller.delete_expired_urls()
	model.delete_expired_urls.assert_called_once()
