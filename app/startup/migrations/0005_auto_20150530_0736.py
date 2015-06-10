# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0004_auto_20150530_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
