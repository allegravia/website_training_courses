# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0003_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='acceptance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='deadline',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
