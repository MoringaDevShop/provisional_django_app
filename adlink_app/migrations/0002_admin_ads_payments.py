# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adlink_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('profile_pic', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='ads/')),
                ('physical_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('payment_for', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
            ],
        ),
    ]
