# Generated by Django 5.1.2 on 2024-11-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='produtoId',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='tipo',
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback_type',
            field=models.CharField(choices=[('RECLAME', 'Reclamação'), ('SUGESTA', 'Sugestão'), ('ELOGIO', 'Elogio')], default='RECLAME', max_length=10),
        ),
    ]
