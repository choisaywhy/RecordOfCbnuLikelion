from django.conf.urls import url
from . import views
from .models import Post,Category,Comment,Recomment
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.models import User

#record/
urlpatterns = [
    url(r'^post_new/$', views.post_new, name="post_new"),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name="post_detail"),    
    url(r'^(?P<post_id>\d+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^(?P<post_id>\d+)/delete/$', views.post_delete, name="post_delete"),
    url(r'^(?P<post_id>\d+)/comment/$', views.comment_new, name="comment_new"),
    url(r'^(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/delete/$', views.comment_delete, name="comment_delete"),
    url(r'^(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/recomment$', views.recomment_new, name="recomment_new"),
    url(r'^(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/recomment/(?P<recomment_id>\d+)/delete/$', views.recomment_delete, name="recomment_delete"),
    url(r'^board/(?P<category_id>\d+)$', views.board, name="board"),
    url(r'^member/$', views.member, name="member"),
    url(r'^introduce/$', views.introduce, name="introduce"),
    url(r'^warning/$', views.warning, name="warning"),
    
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)