"""SCRIPT SERVICE"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from gefapi.errors import EmailError
from sparkpost import SparkPost


class EmailService(object):
    """MailService Class"""

    @staticmethod
    def send_html_email(recipients=[], html='', from_email='test@sparkpostbox.com', subject='[GEF] Undefined Subject'):
        try:
            sp = SparkPost()
            response = sp.transmissions.send(
                recipients=recipients,
                html=html,
                from_email=from_email,
                subject=subject,
                use_sandbox=True
            )
            return response
        except Exception as error:
            raise EmailError(message=str(error))
