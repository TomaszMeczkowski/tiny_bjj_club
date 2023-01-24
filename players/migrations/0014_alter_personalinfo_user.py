# Generated by Django 4.1.4 on 2023-01-24 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0013_remove_player_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinfo",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="players.player",
            ),
        ),
    ]
