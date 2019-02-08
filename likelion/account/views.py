from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('record/main.html')
        else:
            return HttpResponse('error:username or password is incorrect.')
    else:
        return render(request,'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirct('record/main.html')
    return render(request,'account/login.html')