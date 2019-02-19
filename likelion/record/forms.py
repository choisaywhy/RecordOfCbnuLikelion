from django import forms
from .models import Post, Comment, Recomment


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'file', 'text','category') 

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('text',)

class RecommentForm(forms.ModelForm):

    class Meta:
        model = Recomment
        fields = ('text',)

