from django.shortcuts import render
from .models import Player


# Create your views here.


def players(request):

    players_raw = Player.objects.all()
    players = []

    for player in players_raw:
        row = [player.id, player.first_name, player.last_name, player.belt, player.stripes]
        players.append(row)



    context = {"headings": ["Id", "Imie", "Nazwisko", "Pas", "Belki"],
               "data": players,


               }
    return render(request, "players_list.html", context)
