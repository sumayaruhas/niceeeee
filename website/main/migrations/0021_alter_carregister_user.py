# Generated by Django 5.1.3 on 2024-12-21 15:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_carregister_carpic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregister',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
