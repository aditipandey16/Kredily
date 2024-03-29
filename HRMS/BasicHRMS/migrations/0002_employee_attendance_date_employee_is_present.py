# Generated by Django 5.0.1 on 2024-02-01 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasicHRMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='attendance_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
    ]
