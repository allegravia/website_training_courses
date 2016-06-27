# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0022_auto_20160628_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='website',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
