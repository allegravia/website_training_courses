# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0005_course_course_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
