# Generated by Django 5.1.3 on 2025-01-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_booking_customerid_booking_driverid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealstatus',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
