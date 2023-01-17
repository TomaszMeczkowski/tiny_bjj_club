from django.shortcuts import render
from .models import Player
from django.core.paginator import Paginator
from datetime import datetime


# Create your views here.

# TO DO:  rearange local and global variables in players method (keep pagination with players list/search funcionality)
query_players = None


def players(request):

    global query_players
    players = query_players

    if players is None:
        query_players = Player.objects.all()
        players = Player.objects.all()


    pagination_div = 20

    if request.method == "POST":
        # Bad idea but working for some cases (fix it out later)
        first_names = []
        last_names = []
        players = Player.objects.all()
        for i in players:
            first_names.append(i.first_name)
            last_names.append(i.last_name)

        search_bar = request.POST.get("searchbar").capitalize()

        if search_bar in ['Biały', "Niebieski", "Purpurowy", "Brązowy", "Czarny"]:
            players = players.filter(belt=search_bar)
            query_players = players

        elif search_bar in first_names:
            players = players.filter(first_name=search_bar)
            query_players = players

        elif search_bar in last_names:
            players = players.filter(last_name=search_bar)
            query_players = players

        # Case for zero output search
        elif search_bar != "":
            players = players.filter(first_name=search_bar)
            query_players = players

    players = Paginator(players, pagination_div)
    current_page = request.GET.get('page')
    players = players.get_page(current_page)

    context = {"players": players,
               # "query": query_param
               }

    return render(request, "players_list.html", context)


def players_add(request):
    mess = ""
    time_now = datetime.now()
    status = None

    if request.method == "POST":
        first_name = request.POST.get("first_name").capitalize()
        last_name = request.POST.get("last_name").capitalize()

        if first_name != "" and last_name != "":
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


def player_profile_activity(request, player_id):
    player = Player.objects.get(pk=player_id)
    context = {"player": player}
    return render(request, "player_profile_activity.html", context)
