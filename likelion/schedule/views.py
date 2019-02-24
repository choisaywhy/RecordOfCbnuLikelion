
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from django.core.paginator import Paginator


def schedule_this(request):
    return render(request, 'schedule_this.html')

def schedule_all(request):    
    schedule_all = Event.objects.all().order_by('-day')
    page_numbers_range = 10
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(schedule_all,page_numbers_range)
    page = request.GET.get('page')
    events = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]
    
    
    return render(request, 'schedule_all.html',{'schedules':schedule_all,'events':events, 'page_range':page_range, 'paginator':paginator })