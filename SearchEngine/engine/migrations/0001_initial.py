# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aainew',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('tags', models.TextField(blank=True, null=True)),
                ('questions', models.TextField(blank=True, null=True)),
                ('votes', models.TextField(blank=True, null=True)),
                ('no_answers', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aainew',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.TextField(blank=True, null=True)),
                ('questions', models.TextField()),
                ('votes', models.TextField(blank=True, null=True)),
                ('no_answers', models.TextField(blank=True, null=True)),
                ('links', models.TextField()),
            ],
            options={
                'db_table': 'AI',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aicopy',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('tags', models.TextField(blank=True, null=True)),
                ('questions', models.TextField(blank=True, null=True)),
                ('votes', models.TextField(blank=True, null=True)),
                ('no_answers', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aicopy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Askubuntu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.TextField(blank=True, null=True)),
                ('questions', models.TextField()),
                ('votes', models.TextField(blank=True, null=True)),
                ('no_answers', models.TextField(blank=True, null=True)),
                ('links', models.TextField()),
            ],
            options={
                'db_table': 'askUbuntu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Astronomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.TextField(blank=True, null=True)),
                ('questions', models.TextField()),
                ('votes', models.TextField(blank=True, null=True)),
                ('no_answers', models.TextField(blank=True, null=True)),
                ('links', models.TextField()),
            ],
            options={
                'db_table': 'astronomy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('tags', models.TextField(blank=True, null=True)),
                ('questions', models.TextField(blank=True, null=True)),
                ('votes', models.TextField(blank=True, null=True)),
                ('no_answers', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
    ]
