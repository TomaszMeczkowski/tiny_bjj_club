from django.urls import path
from .views import players, players_add, players_test, player_profile


app_name = "players"

urlpatterns = [
    path("", players, name="players_list"),
    path("add", players_add, name="players_add"),
    path("test", players_test, name="players_test"),
    path("test_profile/<int:player_id>", player_profile, name="player_profile"),
]
