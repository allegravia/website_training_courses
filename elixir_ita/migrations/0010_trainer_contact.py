# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0009_trainer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='contact',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
