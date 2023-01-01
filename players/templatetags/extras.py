from django import template


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
def active_player_span(user_id):
    # Under construcion
    if user_id % 3 == 0:
        return "badge badge-soft-danger mb-0"
    else:
        return "badge badge-soft-success mb-0"


@register.simple_tag
def active_player_text(user_id):
    # Under construcion
    if user_id % 3 == 0:
        return 'Nieaktywny'
    else:
        return 'Aktywny'
