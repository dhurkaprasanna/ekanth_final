# Generated by Django 3.1.3 on 2021-03-08 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostelapp', '0021_auto_20210308_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue_raiser',
            name='user',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'student'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue_student',
            name='user',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
