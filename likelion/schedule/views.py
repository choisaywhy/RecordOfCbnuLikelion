from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm


def schedule_this(request):
    return render(request, 'schedule_this.html')

def schedule_all(request):    
    schedule_all = Event.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            schedule_all = form.save(commit=False)
            schedule_all.save()
            return redirect(schedule_all)
    else:
        form = EventForm()
    
    return render(request, 'schedule_all.html',{'schedules':schedule_all, 'form':form})

