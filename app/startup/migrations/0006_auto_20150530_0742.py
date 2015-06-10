# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0005_auto_20150530_0736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='startup',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
