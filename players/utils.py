from .models import Player
from faker import Faker
from random import choice, randint


def create_fake_players(n=1):
    fake = Faker('pl_PL')
    belts = ["Biały", "Niebieski", "Purpurowy", "Brązowy", "Czarny"]
    gender_index = ['M', 'K']

    for _ in range(n):
        choice_input = choice(gender_index)

        if choice_input == "M":
            player = Player(
                first_name=fake.first_name_male(),
                last_name=fake.last_name_male(),
                belt=choice(belts),
                stripe=randint(0, 4),
                gender="Mężczyzna",
                birth_date=fake.date_of_birth(),
            )
            player.save()

        else:
            player = Player(
                first_name=fake.first_name_female(),
                last_name=fake.last_name_female(),
                belt=choice(belts),
                stripe=randint(0, 4),
                gender="Kobieta",
                birth_date=fake.date_of_birth(),
            )
            player.save()


def delete_last_players(n=1):
    for _ in range(n):
        player = Player.objects.last()
        player.delete()


def delete_all_players():
    players_to_bin = Player.objects.all()
    players_to_bin.delete()
