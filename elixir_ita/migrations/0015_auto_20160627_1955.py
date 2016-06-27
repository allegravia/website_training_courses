# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0014_trainer_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='website',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
