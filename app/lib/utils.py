#!/usr/bin/env python3

"""Utility methods for the project."""

__version__ = '0.0.1'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2018, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Production"

import ssl
import smtplib

from app import app

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email, subject, message_text, message_html=''):
    """Send an email with given params."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = "Antari Store"
        message["To"] = receiver_email

        message.attach(MIMEText(message_text, "plain"))
        if message_html:
            message.attach(MIMEText(message_html, "html"))

        server.login(app.config.get('SERVICE_EMAIL'),
                     app.config.get('SERVICE_EMAIL_PWD'))
        server.sendmail(app.config.get('SERVICE_EMAIL'), receiver_email,
                        message.as_string())
