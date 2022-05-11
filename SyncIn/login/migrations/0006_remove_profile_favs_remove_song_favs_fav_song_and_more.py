# Generated by Django 4.0.1 on 2022-05-10 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_fav_remove_profile_favs_song_favs_profile_favs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favs',
        ),
        migrations.RemoveField(
            model_name='song',
            name='favs',
        ),
        migrations.AddField(
            model_name='fav',
            name='song',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='login.song'),
        ),
        migrations.AddField(
            model_name='fav',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='login.profile'),
        ),
    ]
