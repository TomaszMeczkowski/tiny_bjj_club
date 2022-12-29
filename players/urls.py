from django.urls import path
from .views import players


app_name = "players"

urlpatterns = [
    path("", players, name="players_list"),
]
