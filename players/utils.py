from .models import Player
from faker import Faker
from random import choice, randint


def create_fake_players(n=1):
    fake = Faker('pl_PL')
    belts = ["Biały", "Niebieski", "Purpurowy", "Brązowy", "Czarny"]

    for _ in range(n):
        player = Player(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            belt=choice(belts),
            stripe=randint(0, 4),
        )
        player.save()


def delete_last_players(n=1):
    for _ in range(n):
        player = Player.objects.last()
        player.delete()


def delete_all_players():
    players_to_bin = Player.objects.all()
    players_to_bin.delete()
