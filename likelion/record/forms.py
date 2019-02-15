from django import forms
from .models import Post, Comment, Recomment

class PostForm(forms.ModelForm):
    

    class Meta:
        model = Post
        fields = ('title','text','category') 

class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('text',)

class RecommentForm(forms.ModelForm):


    class Meta:
        model = Recomment
        fields = ('text',)
