from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.models import User

urlpatterns = [
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout")  
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)