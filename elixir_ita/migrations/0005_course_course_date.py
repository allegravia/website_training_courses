# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0004_auto_20150908_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
