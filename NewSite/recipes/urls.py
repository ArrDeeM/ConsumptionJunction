from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('signIn/', views.signIn, name='signIn'),
	path('signUp/', views.signUp, name ='signUp'),
]
