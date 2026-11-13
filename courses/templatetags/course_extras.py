from django import template

register = template.Library()

@register.filter
def currency_tnd(value):
    return f"{value} TND"

@register.filter
def categorie_duree(value):
    if value < 10:
        return "Formation courte"
    elif value <= 30:
        return "Formation moyenne"
    else:
        return "Formation longue"