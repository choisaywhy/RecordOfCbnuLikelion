from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields =['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','id','category']
    list_filter=['category']
    list_editable=['category']
    list_display_links=['id','title']
    search_fields = ['title', 'text',]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post_id','post','text','created_at','id',]
    search_fields = ['text',]