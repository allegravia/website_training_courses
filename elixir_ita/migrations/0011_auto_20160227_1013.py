# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_ita', '0010_trainer_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='course_organise',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='course_teach',
            field=models.TextField(blank=True),
        ),
    ]
