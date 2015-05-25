# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(default=b'', max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 5, 25, 9, 36, 21, 457454), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2015, 5, 25, 9, 36, 21, 457490), auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerOptionTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('language', models.ForeignKey(to='userprofile.Language')),
                ('option', models.ForeignKey(to='startup.AnswerOption')),
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
                ('question_nick', models.CharField(default=b'', max_length=50)),
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
            name='QuestionTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('question_hint', models.CharField(default=b'', max_length=200, blank=True)),
                ('language', models.ForeignKey(default=0, to='userprofile.Language')),
                ('question', models.ForeignKey(default=0, to='startup.Question')),
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
                ('name', models.CharField(default=b'', max_length=100)),
                ('logo', models.ImageField(default=b'', upload_to=b'startup/logo')),
                ('profile_image', models.ImageField(default=b'', upload_to=b'startup/logo')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 5, 25, 9, 36, 21, 453892), auto_now_add=True)),
                ('modified_at', models.DateTimeField(null=True, blank=True)),
                ('founder', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StartupMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(default=b'', max_length=200)),
                ('startup', models.ForeignKey(default=0, to='startup.Startup')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StartupStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage', models.CharField(max_length=100)),
                ('rate', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TableAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.IntegerField()),
                ('answer', models.ForeignKey(to='startup.Answer')),
                ('question', models.ForeignKey(to='startup.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='startup',
            name='stage',
            field=models.ForeignKey(to='startup.StartupStage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='question_category',
            field=models.ForeignKey(default=0, to='startup.QuestionCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='question_parent',
            field=models.ForeignKey(blank=True, to='startup.Question', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(default=0, to='startup.QuestionType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='startup_stage',
            field=models.ForeignKey(default=0, to='startup.StartupStage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(to='startup.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_option',
            field=models.ManyToManyField(default=[], to='startup.AnswerOption', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='language',
            field=models.ForeignKey(default=0, to='userprofile.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='public_access',
            field=models.ForeignKey(default=0, to='startup.PublicAccess'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='startup.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='startup',
            field=models.ForeignKey(to='startup.Startup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_by',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
