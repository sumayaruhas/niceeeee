# Generated by Django 5.1.3 on 2024-12-13 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_carregister_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='carregister',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carregister',
            name='carpic',
            field=models.ImageField(blank=True, default='/media/th.jpeg', null=True, upload_to='carpic/'),
        ),
        migrations.AlterField(
            model_name='carregister',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carregister',
            name='profilepic',
            field=models.ImageField(blank=True, default='/media/profile.jpeg', null=True, upload_to='profilepic/'),
        ),
    ]
