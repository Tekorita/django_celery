from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django_celery import settings

@shared_task
def send_emails_users():
    asunto = 'Mensaje de prueba'
    mensaje = 'Bienvenido, este es un mensaje de prueba CELERY; RABBIMQ y DJANGO'
    #users = User.objects.filter(username="Tekorita")
    users = User.objects.all()
    for user in users:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER,[user.email], fail_silently= False)
    return '{} se envio correo correctamente'.format(user)