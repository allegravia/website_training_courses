# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0018_trainer_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='website',
        ),
    ]
