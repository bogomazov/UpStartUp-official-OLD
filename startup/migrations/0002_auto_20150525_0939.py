# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 9, 39, 13, 963053), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 9, 39, 13, 963089), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='startup',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 9, 39, 13, 959953), auto_now_add=True),
            preserve_default=True,
        ),
    ]
