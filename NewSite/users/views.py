from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

def signIn(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(request,username=username,password=password)
    if(user is not None):
        login(request,user)
        messages.success(request,f'Welcome {username}!')
        return redirect('index')
    else:
        messages.error(request,'Invalid login information')
    return render(request, 'login')

def signOut(request):
    logout(request)
    #logout is successful 
    if():
        username = ""
        messages.success(request,f"{username} successfully logged out.")
    return render(request, 'index.html')

def account(request):
    return render(request,'users/account.html')