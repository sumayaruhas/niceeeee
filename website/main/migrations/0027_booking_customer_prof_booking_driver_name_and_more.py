# Generated by Django 5.1.3 on 2025-01-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_dealstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customer_prof',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic/'),
        ),
        migrations.AddField(
            model_name='booking',
            name='driver_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='driver_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='driver_prof',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic/'),
        ),
    ]
