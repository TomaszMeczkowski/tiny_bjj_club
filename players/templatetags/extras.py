from django import template
from ..models import Player


register = template.Library()


@register.simple_tag
def belt_png(belt, stripe):
    belts = {"Biały": 1,
             "Niebieski": 2,
             "Purpurowy": 3,
             "Brązowy": 4,
             "Czarny": 5}

    belt_index = belts[belt]

    result = f"/static/images/belts/{belt_index}.{stripe}.{belt}.png"
    return result


@register.simple_tag
def email_display(user_id):
    player = Player.objects.get(pk=user_id)
    email = player.personalinfo.email
    if email:
        return email
    else:
        return "Brak"

