from django.urls import path
from .views import index, about, contact, about_project


app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name='about'),
    path('kontakt/', contact, name='contact'),
    path("projekt/", about_project, name="about_project")
]
