# Generated by Django 3.0 on 2020-12-22 14:54

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('blog', '0009_auto_20201218_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySuperuser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
