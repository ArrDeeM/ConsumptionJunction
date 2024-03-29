from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from recipes.models import Recipe
from django.contrib import messages
from recipes.forms import RecipeForm

def index(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipe_list})

def aboutUs(request):
    return render(request, 'recipes/aboutUs.html')

def recipeView(request, recipe_url):
    try:
        recipe = Recipe.objects.get(recipe_url=recipe_url)
    except Recipe.DoesNotExist:
        pass
    return render(request, 'recipes/recipeView.html', {'recipe':recipe})

def makeRecipe(request):
    #if(not request.user.is_authenticated()):
    #    messages.error(request, 'You must be logged in to make a recipe.')
    #    return redirect('login')
    form = RecipeForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = RecipeForm()
    return render(request, 'recipes/makeRecipe.html', {'form':form})
