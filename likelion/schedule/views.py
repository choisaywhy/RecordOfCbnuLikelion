from django.shortcuts import render, get_object_or_404, redirect
from .models import Event


def schedule_this(request):
    return render(request, 'schedule_this.html')

def schedule_all(request):    
    schedule_all = Event.objects.all()
    return render(request, 'schedule_all.html',{'schedules':schedule_all})

