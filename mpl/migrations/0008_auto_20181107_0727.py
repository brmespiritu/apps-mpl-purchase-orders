# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 07:27
from __future__ import unicode_literals

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('mpl', '0007_auto_20181107_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpurchaseorder',
            name='status',
            field=django_mysql.models.EnumField(choices=[('PENDING', 'Pending'), ('IN_TRANSIT', 'In Transit'), ('DELIVERED', 'Delivered')], default='PENDING'),
        ),
        migrations.AlterField(
            model_name='mplpurchaseorder',
            name='status',
            field=django_mysql.models.EnumField(choices=[('PENDING', 'Pending'), ('IN_TRANSIT_TO_WAREHOUSE', 'In Transit to Warehouse'), ('IN_TRANSIT_TO_MANILA', 'In Transit to Manila'), ('AT_WAREHOUSE', 'At Warehouse'), ('DELIVERED', 'Delivered')], default='PENDING'),
        ),
    ]