# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0003_auto_20150527_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'startup/logo'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=b'startup/logo'),
        ),
    ]
