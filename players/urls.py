from django.urls import path
from .views import players, players_add, players_test


app_name = "players"

urlpatterns = [
    path("", players, name="players_list"),
    path("add", players_add, name="players_add"),
    path("test", players_test, name="players_test"),
]
