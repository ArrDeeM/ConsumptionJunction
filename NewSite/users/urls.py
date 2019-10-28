from django.urls import path
from . import views

urlpatterns = [
    
    path('signIn/', views.signIn, name='signIn'),
	path('register/', views.register, name ='register'),
    path('account/', views.account, name='account'),
]