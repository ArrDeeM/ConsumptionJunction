from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

recipes = [
    {
        'User' : 'Zach',
        'Recipe' : 'Bacon Pancakes',
        'Ingrediants' : ['Bacon','flower'],
        'Directions' : 'make em',
        
    },
    {
        'User' : 'Clayton',
        'Recipe' : 'Blueberry Pancakes',
        'Ingrediants' : ['Blueberries','flower',],
        'Directions' : 'cook em',
    }
]

def index(request):
    context = {
        'recipes' : recipes
    }
    return render(request, 'recipes/index.html', context)

def aboutUs(request):
    return render(request, 'recipes/aboutUs.html')
