from django.urls import path
from .views import players, players_add, player_profile
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


app_name = "players"

urlpatterns = [
    path("", players, name="players_list"),
    path("dodaj", players_add, name="players_add"),
    path("profil/<int:player_id>", player_profile, name="player_profile"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('imgages/favicon.png')))
]
