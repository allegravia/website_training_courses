# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0015_auto_20160627_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='website',
            field=models.CharField(default=b'-', max_length=400, blank=True),
        ),
    ]
