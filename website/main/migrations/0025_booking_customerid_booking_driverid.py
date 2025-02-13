# Generated by Django 5.1.3 on 2025-01-13 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_booking_age_booking_dropoff_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customerid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_bookings', to='main.riderregister'),
        ),
        migrations.AddField(
            model_name='booking',
            name='driverid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_bookings', to='main.carregister'),
        ),
    ]
