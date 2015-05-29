# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20150529_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='current_language',
            field=models.ForeignKey(to='userprofile.Language', null=True),
        ),
    ]
