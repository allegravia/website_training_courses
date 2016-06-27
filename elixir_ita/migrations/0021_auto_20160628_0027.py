# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elixir_ita', '0020_trainer_ciccio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer2',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('code', models.CharField(max_length=80, serialize=False, primary_key=True)),
                ('keywords', models.CharField(max_length=400, null=True, blank=True)),
                ('bio', models.TextField(blank=True)),
                ('affiliation', models.CharField(max_length=400, null=True, blank=True)),
                ('ciccio', models.CharField(max_length=400, null=True, blank=True)),
                ('photo', models.CharField(max_length=80, null=True, blank=True)),
                ('contact', models.CharField(max_length=400, null=True, blank=True)),
                ('course_teach', models.TextField(blank=True)),
                ('course_organise', models.TextField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='ciccio',
        ),
    ]
