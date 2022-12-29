from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"message": ""}
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def about_project(request):
    context = {}
    return render(request, "about_project.html", context)
