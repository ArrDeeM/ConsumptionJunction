from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name ='aboutUs'),
    path('recipe/<recipe_url>/', views.recipeView, name ='recipeView'),
    path('account/makeRecipe/', views.makeRecipe, name = 'makeRecipe'),
]
