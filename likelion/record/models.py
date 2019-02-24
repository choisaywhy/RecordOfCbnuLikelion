from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return '%s by %s' % (self.title, self.name_id)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"post_id": self.id})

    @property
    def count_comments(self):
        comments = self.comment_set.count()
        recomments = 0
        for comment in self.comment_set.all():
            recomments += comment.recomment_set.count()
        return comments + recomments


#모델.쿼리셋.메소드
class Comment(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text


class Recomment(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text