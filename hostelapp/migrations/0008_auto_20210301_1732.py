# Generated by Django 3.1.3 on 2021-03-01 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0007_auto_20210301_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatepass',
            name='applied_date',
        ),
        migrations.RemoveField(
            model_name='gatepass',
            name='count',
        ),
    ]