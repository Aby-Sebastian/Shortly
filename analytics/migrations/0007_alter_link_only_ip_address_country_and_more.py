# Generated by Django 4.0.3 on 2022-11-14 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_remove_analytics_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link_only_ip_address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.countries'),
        ),
        migrations.AlterField(
            model_name='link_only_ip_address',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.devices'),
        ),
        migrations.AlterField(
            model_name='link_only_ip_address',
            name='ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.ip_address'),
        ),
    ]
