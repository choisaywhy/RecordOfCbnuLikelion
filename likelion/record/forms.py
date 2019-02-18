from django import forms
from .models import Post, Comment, Recomment
from django.contrib.auth import models as auth_models

class PostForm(forms.ModelForm):
    

    class Meta:
        model = Post
        fields = ('title', 'file', 'text','category') 

    def __init(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False

class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('text',)

class RecommentForm(forms.ModelForm):


    class Meta:
        model = Recomment
        fields = ('text',)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',}))
