from django.urls import path
from .views import players, players_add, player_profile


app_name = "players"

urlpatterns = [
    path("", players, name="players_list"),
    path("dodaj", players_add, name="players_add"),
    path("profil/<int:player_id>", player_profile, name="player_profile"),
]
