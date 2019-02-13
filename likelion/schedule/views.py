from django.shortcuts import render, get_object_or_404, redirect

def schedule_this(request):
    return render(request, 'schedule_this.html')

def schedule_all(request):
    return render(request, 'schedule_all.html')