# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tagline',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='access_token',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=b'', upload_to=b'static/files/user/avatar'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar_url',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_language',
            field=models.ForeignKey(default=0, to='userprofile.Language'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='expires_in',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='headline',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='industry',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='summary',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(default=1, to='userprofile.UserType'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='auth_type',
            field=models.ForeignKey(default=1, to='userprofile.AuthType'),
        ),
    ]
