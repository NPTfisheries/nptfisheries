from django import forms
from django.db.migrations.state import get_related_models_tuples
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'snippet', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog title'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-select', 'size':10}),
            'header_image': forms.FileInput(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Provide a short description of the blog.', 'rows':5}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Main body of the blog.', 'rows':5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        

        fields = ['content','parent']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(),
        }