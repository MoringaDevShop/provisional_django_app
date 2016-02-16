# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adlink_app', '0002_admin_ads_payments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='role',
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(  to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='profile_pic',
            field=models.FileField(upload_to='profile_pics', blank=True),
        ),
    ]
