from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import (login as django_login, authenticate, logout as django_logout)

def login(request):
    if request.method =='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username =login_form.cleaned_data['username']
            password =login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                django_login(request,user)
                return redirect('main')
            # else:
            # #     return HttpResponse('웅틀렷움')
            else:
                return HttpResponse('틀렷움')
    else:
        login_form = LoginForm(request.POST)
        return render(request,'account/login.html', {'login_form': login_form})


def logout(request):
        django_logout(request)
        return redirect('login')   