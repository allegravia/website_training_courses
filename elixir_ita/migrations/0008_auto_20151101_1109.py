# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0007_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='acceptance',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='affiliation',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='code',
            field=models.CharField(max_length=80, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='keywords',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
