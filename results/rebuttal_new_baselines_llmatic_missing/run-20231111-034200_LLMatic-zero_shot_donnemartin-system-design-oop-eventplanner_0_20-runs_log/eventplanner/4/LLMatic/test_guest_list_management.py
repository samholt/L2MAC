import pytest
import guest_list_management

def test_guest_list_management():
	gl_management = guest_list_management.GuestListManagement()
	gl_management.create_guest_list('event1')
	assert 'event1' in gl_management.guest_lists

	guest = guest_list_management.Guest('John Doe', 'Not Responded')
	gl_management.add_guest('event1', guest)
	assert gl_management.guest_lists['event1'][0].name == 'John Doe'

	gl_management.update_guest('event1', 'John Doe', 'Attending')
	assert gl_management.guest_lists['event1'][0].rsvp_status == 'Attending'

	guest_list = gl_management.view_guest_list('event1')
	assert len(guest_list) == 1

	new_guest_list = [guest_list_management.Guest('Jane Doe', 'Not Responded')]
	gl_management.import_guest_list('event1', new_guest_list)
	assert gl_management.guest_lists['event1'][0].name == 'Jane Doe'

	exported_guest_list = gl_management.export_guest_list('event1')
	assert len(exported_guest_list) == 1
