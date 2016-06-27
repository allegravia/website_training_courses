# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0021_auto_20160628_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer2',
            name='author',
        ),
        migrations.DeleteModel(
            name='Trainer2',
        ),
    ]
