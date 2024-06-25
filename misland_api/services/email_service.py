"""SCRIPT SERVICE"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from misland_api.config import SETTINGS
from misland_api.errors import EmailError
# from sparkpost import SparkPost
from flask import Flask
from flask_mail import Mail, Message
import os

EMAIL_CONFIGS = SETTINGS.get('environment', {})

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": EMAIL_CONFIGS['EMAIL_SERVER'],
    "MAIL_PORT": EMAIL_CONFIGS['EMAIL_PORT'],
    "MAIL_USE_TLS":EMAIL_CONFIGS['EMAIL_USE_TLS'],
    "MAIL_USE_SSL": EMAIL_CONFIGS['EMAIL_USE_SSL'],
    "MAIL_USERNAME": EMAIL_CONFIGS['EMAIL_USER'],
    "MAIL_PASSWORD": EMAIL_CONFIGS['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)

class EmailService(object):
    """MailService Class"""
    
    @staticmethod
    def send_html_email(recipients=[], html='', sender=app.config.get("MAIL_USERNAME"), subject='[MISLAND] Undefined Subject'):
        try:
            
            with app.app_context():
                response = Message(
                    recipients = recipients,
                    html = html,
                    sender = sender,
                    subject = subject
                )
                logging.info('{}'.format(response))
                mail.send(response)
            # sp = SparkPost()
            # response = sp.transmissions.send(
            #     recipients=recipients,
            #     html=html,
            #     from_email=from_email,
            #     subject=subject
            # )
            # return response
        except Exception as error:
            logging.error(error)
            raise EmailError(message=error)
