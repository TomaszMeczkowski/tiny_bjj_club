from django.urls import path
from .views import players, players_add, player_profile, player_profile_biling, player_profile_activity


app_name = "players"

urlpatterns = [
    path("", players, name="players_list"),
    path("dodaj", players_add, name="players_add"),
    path("profil/<int:player_id>", player_profile, name="player_profile"),
    path("profil/<int:player_id>/biling", player_profile_biling, name="player_profile_biling"),
    path("profil/<int:player_id>/activity", player_profile_activity, name="player_profile_activity"),
]
