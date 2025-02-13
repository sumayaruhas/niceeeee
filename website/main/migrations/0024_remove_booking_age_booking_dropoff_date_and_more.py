# Generated by Django 5.1.2 on 2024-12-23 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_riderregister_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='age',
        ),
        migrations.AddField(
            model_name='booking',
            name='dropoff_date',
            field=models.DateField(default=datetime.date(1999, 10, 10)),
        ),
        migrations.AddField(
            model_name='booking',
            name='dropoff_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_date',
            field=models.DateField(default=datetime.date(1999, 10, 10)),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
