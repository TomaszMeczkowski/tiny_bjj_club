# Generated by Django 4.1.4 on 2023-01-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0005_player_first_training_player_last_training"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="first_training",
            field=models.DateField(blank=True, null=True),
        ),
    ]