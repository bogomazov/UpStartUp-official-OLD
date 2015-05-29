# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20150529_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='auth_type',
            field=models.ForeignKey(to='userprofile.AuthType', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(to='userprofile.UserType', null=True),
        ),
    ]
