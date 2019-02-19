from django import forms
from .models import Post, Comment, Recomment


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

