# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0012_course_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
