from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    msg = Message('Reset Your Password',
                  sender=current_app.config['ADMINS'][0],
                  recipients=[user.email])
    msg.body = render_template('email/reset_password.txt',
                               user=user, token=token)
    msg.html = render_template('email/reset_password.html',
                               user=user, token=token)
    mail.send(msg)
