# Generated by Django 5.1.2 on 2024-11-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0005_alter_convite_convite_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convite',
            name='limiteConvites',
            field=models.IntegerField(default=1),
        ),
    ]