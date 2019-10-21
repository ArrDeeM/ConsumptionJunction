from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from recipes.models import Recipe

def index(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipe_list})

def aboutUs(request):
    return render(request, 'recipes/aboutUs.html')

class RecipeView(generic.ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    template_name = "recipes/index.html"

    def get_queryset(self):
        return Recipe.objects.all()
