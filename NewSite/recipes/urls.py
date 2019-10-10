from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name ='aboutUs'),
]
