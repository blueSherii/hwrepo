# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-05 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwrepo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaseweb',
            name='contract_internalReference',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='leaseweb',
            name='contract_reference',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
