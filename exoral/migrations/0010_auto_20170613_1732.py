# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exoral', '0009_protokoll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exoraluser',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='testat',
            options={'ordering': ('bezeichnung',), 'verbose_name': 'mündl. Testat', 'verbose_name_plural': 'mündl. Testate'},
        ),
        migrations.AlterModelOptions(
            name='textbeitrag',
            options={'ordering': ('-created_date',)},
        ),
        migrations.DeleteModel(
            name='ExoralUser',
        ),
    ]
