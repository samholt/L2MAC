import pytest
from guests import Guest

def test_guest_management():
	guest = Guest()
	guest.add_guest('John Doe', 'Yes')
	assert guest.view_guests() == {'John Doe': 'Yes'}
	guest.update_guest('John Doe', 'No')
	assert guest.view_guests() == {'John Doe': 'No'}
	guest.import_guests({'Jane Doe': 'Yes'})
	assert guest.view_guests() == {'Jane Doe': 'Yes'}
	assert guest.export_guests() == {'Jane Doe': 'Yes'}
