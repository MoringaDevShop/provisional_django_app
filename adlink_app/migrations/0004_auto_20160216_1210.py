# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adlink_app', '0003_auto_20160212_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='company',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='firstname',
            field=models.CharField(default=datetime.datetime(2016, 2, 16, 12, 9, 10, 680958, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='lastname',
            field=models.CharField(default=datetime.datetime(2016, 2, 16, 12, 10, 14, 583005, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='profile_pic',
            field=models.FileField(upload_to='profile_pics'),
        ),
    ]
