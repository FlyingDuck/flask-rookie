# -*- coding: utf-8 -*-

from app.extensions import celery, mail

from flask_mail import Message

@celery.task
def send_async_email(subject, sender, recipients, html):
    msg = Message(subject=subject, sender=sender, recipients=recipients, html=html)
    mail.send(msg)
