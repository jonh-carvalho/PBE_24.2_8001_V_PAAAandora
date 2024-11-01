# Generated by Django 5.1.2 on 2024-11-01 13:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('dataCriacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('validade', models.DateTimeField()),
                ('estado', models.CharField(default='enviado', max_length=50)),
                ('limiteConvites', models.IntegerField(default=1)),
            ],
        ),
    ]