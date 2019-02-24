from django import forms
from django.forms import ModelForm, TextInput
from .models import Post, Comment, Recomment



class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'file', 'text','category']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):

    
    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'text': TextInput(attrs={'class':'form-control'}),
        }
        

           


class RecommentForm(forms.ModelForm):

    class Meta:
        model = Recomment
        fields = ['text',]
        widgets = {
            'text': TextInput(attrs={'class':'form-control form-control-lg'}),
        }


