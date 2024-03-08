import pytest
from sharing import Sharing

def test_sharing_share():
	sharing = Sharing(1, 1, 'read')
	sharing.share(2, 'write')
	assert sharing.shared_files[1][2] == 'write'

def test_sharing_unshare():
	sharing = Sharing(1, 1, 'read')
	sharing.share(2, 'write')
	sharing.unshare(2)
	assert 2 not in sharing.shared_files[1]

