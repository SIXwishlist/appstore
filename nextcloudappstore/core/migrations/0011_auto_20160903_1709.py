# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-03 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160829_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appratingtranslation',
            name='comment',
            field=models.TextField(blank=True, default='', help_text='Rating comment in Markdown', verbose_name='Rating comment'),
        ),
    ]