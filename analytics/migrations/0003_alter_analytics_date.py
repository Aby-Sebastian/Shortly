# Generated by Django 4.0.3 on 2022-09-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_alter_analytics_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
