from django.urls import path

from . import views

urlpatterns = [
    path('signin/', views.signIn, name='accountSignIn'),
    path('signup/', views.signUp, name='accountSignUp'),
    path('', views.index, name='index'),
]
