from gcs_project.app.models import User


def add_is_active_attribute():
    if not hasattr(User, 'is_active'):
        User.is_active = property(lambda self: self.active)


add_is_active_attribute()