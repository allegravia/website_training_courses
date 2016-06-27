# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0016_auto_20160627_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='website',
        ),
    ]
