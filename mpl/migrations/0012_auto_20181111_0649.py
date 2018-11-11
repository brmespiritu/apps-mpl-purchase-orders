# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-11 06:49
from __future__ import unicode_literals

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('mpl', '0011_mplquotationitem_multiplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientpurchaseorder',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
        migrations.AddField(
            model_name='clientpurchaseorderitem',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
        migrations.AddField(
            model_name='mplpurchaseorder',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
        migrations.AddField(
            model_name='mplpurchaseorderitem',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
        migrations.AddField(
            model_name='mplquotation',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
        migrations.AddField(
            model_name='mplquotationitem',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
        migrations.AddField(
            model_name='supplierquotation',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
        migrations.AddField(
            model_name='supplierquotationitem',
            name='currency',
            field=django_mysql.models.EnumField(choices=[('USD', 'USD (US$)'), ('EUR', 'EUR (\u20ac)'), ('GBP', 'GBP (\xa3)')], default='USD'),
        ),
    ]