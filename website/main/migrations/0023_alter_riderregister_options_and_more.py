# Generated by Django 5.1.3 on 2024-12-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_riderregister'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='riderregister',
            options={'verbose_name': 'Rider Registration', 'verbose_name_plural': 'Riders Registrations'},
        ),
        migrations.AlterField(
            model_name='riderregister',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
