# Generated by Django 5.1.2 on 2024-10-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryhello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
