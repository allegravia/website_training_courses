# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0019_remove_trainer_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='ciccio',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
