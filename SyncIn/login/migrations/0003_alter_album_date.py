# Generated by Django 4.0.1 on 2022-05-10 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_album_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.IntegerField(default=2022, null=True),
        ),
    ]
