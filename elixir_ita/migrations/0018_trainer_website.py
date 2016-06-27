# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0017_remove_trainer_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='website',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
