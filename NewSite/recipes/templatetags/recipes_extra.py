from django import template
from recipes.models import Recipe

register = template.Library()

def add(text):
    r = Recipe(recipe_name = text)
    r.save()
