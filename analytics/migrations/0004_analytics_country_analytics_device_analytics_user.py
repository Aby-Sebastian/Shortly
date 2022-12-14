# Generated by Django 4.0.3 on 2022-11-14 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0003_alter_analytics_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='analytics.countries'),
        ),
        migrations.AddField(
            model_name='analytics',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='analytics.devices'),
        ),
        migrations.AddField(
            model_name='analytics',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
