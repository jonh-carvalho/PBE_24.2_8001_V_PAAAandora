# Generated by Django 5.1.2 on 2024-11-08 14:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_app', '0003_alter_feedback_datahoraenvio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='dataHoraEnvio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
