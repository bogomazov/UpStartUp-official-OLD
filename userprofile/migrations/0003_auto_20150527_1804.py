# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20150527_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='current_language',
            field=models.ForeignKey(default=1, to='userprofile.Language'),
        ),
    ]
