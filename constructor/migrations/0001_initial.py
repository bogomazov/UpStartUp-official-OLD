# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(default=b'', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=100)),
                ('permission_rate', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('question_name', models.CharField(default=b'', max_length=200)),
                ('question_hint', models.CharField(default=b'', max_length=200, blank=True)),
                ('is_optional', models.BooleanField(default=False)),
                ('question_order', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_category_title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StartupMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_position', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=100)),
                ('last_name', models.CharField(default=b'', max_length=100)),
                ('avatar_url', models.CharField(default=b'', max_length=100)),
                ('country', models.CharField(default=b'', max_length=100)),
                ('headline', models.CharField(default=b'', max_length=100)),
                ('industry', models.CharField(default=b'', max_length=100)),
                ('summary', models.CharField(default=b'', max_length=500)),
                ('expires_in', models.CharField(default=b'', max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='startupmember',
            name='user',
            field=models.ForeignKey(to='constructor.UserProfile', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='startup',
            name='co_founder',
            field=models.ManyToManyField(to='constructor.StartupMember', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='startup',
            name='founder',
            field=models.ForeignKey(to='constructor.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='question_category',
            field=models.ForeignKey(default=0, to='constructor.QuestionCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(default=0, to='constructor.QuestionType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(to='constructor.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='public_access',
            field=models.ForeignKey(default=0, to='constructor.PublicAccess'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='constructor.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='startup',
            field=models.ForeignKey(to='constructor.Startup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
