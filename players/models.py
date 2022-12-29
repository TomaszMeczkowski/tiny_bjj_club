from django.db import models


# Create your models here.


class Player(models.Model):

    class Belts(models.TextChoices):
        WHITE = "Biały", "Biały"
        BLUE = "Niebieski", "Niebieski"
        PURPLE = "Purpurowy", "Purpurowy"
        BROWN = "Brązowy", "Brązowy"
        BLACK = "Czarny", "Czarny"

    class Stripes(models.TextChoices):
        ZERO = "0", "0"
        ONE = "1", "1"
        TWO = "2", "2"
        THREE = "3", "3"
        FOUR = "4", "4"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    belt = models.CharField(max_length=30, choices=Belts.choices, default=Belts.WHITE)
    stripes = models.CharField(max_length=1, choices=Stripes.choices, default=Stripes.ZERO)

    def __str__(self):
        return f"{self.id}. {self.first_name} {self.last_name}"
