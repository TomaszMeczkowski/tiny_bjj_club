# Generated by Django 4.1.4 on 2023-01-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0007_rename_player_created_player_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
