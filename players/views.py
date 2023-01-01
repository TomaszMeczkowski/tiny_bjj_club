from django.shortcuts import render
from .models import Player


# Create your views here.


def players(request):
    players_raw = Player.objects.all()
    players = []

    # for i in enumerate(players_raw):
    #     players.append(players_raw[i])

    for i in range(len(players_raw)):
        players.append(players_raw[i])

    context = {"headings": ["Id", "Imie i Nazwisko", "Pas", "Belki"],
               "players": players,
               }

    return render(request, "players_list.html", context)


def players_add(request):
    context = {"message": "",
               }
    return render(request, "players_add.html", context)


def players_test(request):
    players = Player.objects.all()
    count_players = len(players)

    context = {"count_players": count_players,
               "players": players,
               }
    return render(request, "test/test_player_table.html", context)


def player_profile(request, player_id):
    player = Player.objects.get(pk=player_id)
    context = {"player": player}
    return render(request, "test/player_profile_01.html", context)
