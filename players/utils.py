from .models import Player, PersonalInfo, MembershipFee
from faker import Faker
from random import choice, randint


def create_fake_players(n=1):
    fake = Faker('pl_PL')
    belts = ["Biały", "Niebieski", "Purpurowy", "Brązowy", "Czarny"]
    gender_index = ['M', 'K']

    for _ in range(n):
        choice_input = choice(gender_index)

        if choice_input == "M":
            gender = "Mężczyzna"
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()

        else:
            gender = "Kobieta"
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()

        player = Player(
            first_name=first_name,
            last_name=last_name,
            belt=choice(belts),
            stripe=randint(0, 4),
        )
        player.save()

        player = Player.objects.last().id

        player_info = PersonalInfo(player,
                                   gender=gender,
                                   birth_date=fake.date_of_birth(),
                                   email=fake.free_email(),
                                   phone_number=fake.phone_number(),
                                   )
        player_info.save()

        player_sub = MembershipFee(player,
                                   active=randint(0, 1),
                                   )
        player_sub.save()


def delete_last_players(n=1):
    for _ in range(n):
        player = Player.objects.last()
        player.delete()


def delete_all_players():
    players_to_bin = Player.objects.all()
    players_to_bin.delete()

