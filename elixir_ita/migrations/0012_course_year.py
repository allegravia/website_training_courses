# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0011_auto_20160227_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
