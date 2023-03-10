# Generated by Django 4.1.4 on 2022-12-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "belt",
                    models.CharField(
                        choices=[
                            ("Biały", "Biały"),
                            ("Niebieski", "Niebieski"),
                            ("Purpurowy", "Purpurowy"),
                            ("Brązowy", "Brązowy"),
                            ("Czarny", "Czarny"),
                        ],
                        default="Biały",
                        max_length=30,
                    ),
                ),
                (
                    "stripe",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                        ],
                        default="0",
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]
