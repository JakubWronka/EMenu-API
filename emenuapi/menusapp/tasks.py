from .models import Menu, Recipe
from .serializers import MenuSerializer, RecipeSerializer
from django.contrib.auth.models import User
from django.core.mail import send_mail

from celery import shared_task

from datetime import datetime, timedelta, timezone

import json

from smtplib import SMTPException

@shared_task
def send_mail_recently_modified_data():
    mail_data = []
    current_datetime = datetime.now(timezone.utc) 
    menus = Menu.objects.all()
    recipes = Recipe.objects.all()
    mail_data.append('Newly modified menus:')
    for menu in menus:
        if current_datetime - menu.modified < timedelta(hours=24):
            mail_data.append(MenuSerializer(menu).data)
    mail_data.append('Newly modified recipes:')
    for recipe in recipes:
        if current_datetime - recipe.modified < timedelta(hours=24):
            mail_data.append(RecipeSerializer(recipe).data)
    try:
        send_mail(
            subject='Check out this new menus and recipes!',
            message=json.dumps(mail_data),
            from_email='my_django_email@mailing.com',
            recipient_list=[user.email for user in User.objects.all()],
            auth_user='my_django_email',
            auth_password='my_secret_password',
            fail_silently=False
        )
        return 'E-mails sent successfully'
    except SMTPException:
        return 'There was a problem while sending e-mails'
    except:
        return 'Something went wrong, unknown cause'
