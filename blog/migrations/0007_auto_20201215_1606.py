# Generated by Django 3.0 on 2020-12-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
