# Generated by Django 5.0.2 on 2025-05-31 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music_logs', '0002_initial'),
        ('music_ratings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='winner_song_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winning_ratings', to='music_logs.songlog'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'song_log', 'compared_song_log')},
        ),
    ]
