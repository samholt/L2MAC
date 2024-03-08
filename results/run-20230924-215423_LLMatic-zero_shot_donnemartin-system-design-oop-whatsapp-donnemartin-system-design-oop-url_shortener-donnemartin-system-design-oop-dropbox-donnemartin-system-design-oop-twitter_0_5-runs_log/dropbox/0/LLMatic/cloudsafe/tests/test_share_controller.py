from cloudsafe.controllers import share_controller


def test_share():
	assert share_controller.share() == 'Share'

def test_invite():
	assert share_controller.invite() == 'Invite'

