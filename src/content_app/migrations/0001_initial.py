# Generated by Django 5.1.2 on 2024-10-24 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file_url', models.URLField()),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('content_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video')], max_length=10)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=True)),
                ('status', models.CharField(default='published', max_length=20)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
