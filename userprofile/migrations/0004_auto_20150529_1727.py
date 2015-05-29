# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20150527_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='auth_type',
            field=models.ForeignKey(to='userprofile.AuthType', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(to='userprofile.UserType', blank=True),
        ),
    ]
