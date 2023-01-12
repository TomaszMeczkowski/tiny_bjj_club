from django.shortcuts import render
from .models import Player
from django.core.paginator import Paginator
from datetime import datetime


# Create your views here.


def players(request):
    players = Player.objects.all()

    # Very bad idea but working for some cases (work it out later)
    first_names = []
    last_names = []
    for i in players:
        first_names.append(i.first_name)
        last_names.append(i.last_name)

    if request.method == "POST":
        search_bar = request.POST.get("searchbar").capitalize()

        if search_bar in ['Biały', "Niebieski", "Purpurowy", "Brązowy", "Czarny"]:
            players = players.filter(belt=search_bar)

        elif search_bar in first_names:
            players = players.filter(first_name=search_bar)

        elif search_bar in last_names:
            players = players.filter(last_name=search_bar)

        # Case for zero output search
        elif search_bar != "":
            players = players.filter(first_name=search_bar)

    players = Paginator(players, 20)
    count_players = players.count
    current_page = request.GET.get('page')
    players = players.get_page(current_page)

    context = {"count_players": count_players,
               "players": players,
               }
    return render(request, "players_list.html", context)


def players_add(request):
    mess = ""
    time_now = datetime.now()
    status = None

    if request.method == "POST":
        first_name = request.POST.get("first_name").capitalize()
        last_name = request.POST.get("last_name").capitalize()
        belt = request.POST.get("belt")
        stripe = request.POST.get("stripe")
        gender = request.POST.get("gender")
        mess = f"{first_name} {last_name}"
        status = "added"

        player = Player(first_name=first_name,
                        last_name=last_name,
                        belt=belt,
                        stripe=stripe,
                        gender=gender,
                        )
        player.save()

    context = {"message": mess,
               "status": status,
               "time_now": time_now,
               }
    return render(request, "players_add.html", context)


def player_profile(request, player_id):
    player = Player.objects.get(pk=player_id)

    if request.method == "POST":
        first_name = request.POST.get("first_name").capitalize()
        last_name = request.POST.get("last_name").capitalize()
        gender = request.POST.get("gender")
        print(first_name, last_name, gender)

        player.first_name = first_name
        player.last_name = last_name
        player.gender = gender

        player.save()

    context = {"player": player}
    return render(request, "player_profile.html", context)


def player_profile_biling(request, player_id):
    player = Player.objects.get(pk=player_id)
    context = {"player": player}
    return render(request, "player_profile_biling.html", context)
