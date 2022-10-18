from django import forms
from django.db.migrations.state import get_related_models_tuples
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'author', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'This is the title'}),
            'uploaded_by': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
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