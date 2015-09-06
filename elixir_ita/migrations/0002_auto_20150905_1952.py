# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='data',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='venue',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
