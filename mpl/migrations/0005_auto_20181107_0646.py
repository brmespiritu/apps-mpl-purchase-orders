# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 06:46
from __future__ import unicode_literals

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('mpl', '0004_auto_20181105_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpurchaseorder',
            name='status',
            field=django_mysql.models.EnumField(choices=[('IN_TRANSIT', 'In Transit'), ('AT_WAREHOUSE', 'At Warehouse'), ('DELIVERED', 'Delivered')]),
        ),
        migrations.AlterField(
            model_name='mplpurchaseorder',
            name='status',
            field=django_mysql.models.EnumField(choices=[('IN_TRANSIT', 'In Transit'), ('AT_WAREHOUSE', 'At Warehouse'), ('DELIVERED', 'Delivered')]),
        ),
        migrations.AlterField(
            model_name='mplquotation',
            name='status',
            field=django_mysql.models.EnumField(choices=[('PENDING', 'Pending'), ('AWARDED', 'Awarded'), ('LOST', 'Lost')]),
        ),
        migrations.AlterField(
            model_name='supplierquotation',
            name='status',
            field=django_mysql.models.EnumField(choices=[('UNDER_REVIEW', 'Under Review'), ('AWARDED', 'Awarded'), ('REJECTED', 'Rejected')], default='UNDER_REVIEW'),
        ),
    ]