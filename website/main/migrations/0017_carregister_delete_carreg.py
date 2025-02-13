# Generated by Django 5.1.3 on 2024-12-12 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_booking_is_approved_booking_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(blank=True, default='/static/website/images/profile.jpeg', null=True, upload_to='profilepic/')),
                ('carpic', models.ImageField(blank=True, default='/static/website/images/th.jpeg', null=True, upload_to='carpic/')),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('district', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('Transportation', models.BooleanField(default=False)),
                ('gender', models.CharField(default='', max_length=100)),
                ('brand', models.CharField(default='', max_length=100)),
                ('model', models.CharField(default='', max_length=100)),
                ('reg_area_code', models.CharField(default='', max_length=100)),
                ('reg_cat', models.CharField(default='9', max_length=100)),
                ('selected_date', models.DateField(default=datetime.date(1999, 10, 10))),
                ('phonenumber', models.CharField(default='', max_length=15)),
                ('license_no', models.CharField(default='', max_length=20)),
                ('reg_digits', models.CharField(default='', max_length=10)),
                ('nid', models.CharField(default='n/a', max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('reg_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Car Driver Registration',
                'verbose_name_plural': 'Car Driver Registrations',
            },
        ),
        migrations.DeleteModel(
            name='CarReg',
        ),
    ]
