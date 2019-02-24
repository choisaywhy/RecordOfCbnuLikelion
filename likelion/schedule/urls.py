from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'this/', views.schedule_this, name="schedule_this"),
    url(r'all/', views.schedule_all, name="schedule_all"),

 
]