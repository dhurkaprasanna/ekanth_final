# Generated by Django 3.1.3 on 2021-03-08 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0022_auto_20210308_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue_student',
            name='issueid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hostelapp.issue_raiser'),
        ),
        migrations.AlterField(
            model_name='issue_student',
            name='upvote',
            field=models.BooleanField(null=True),
        ),
    ]
