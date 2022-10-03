from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'uploaded_by', 'primary_author', 'secondary_authors', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'This is the title'}),
            'uploaded_by': forms.Select(attrs={'class': 'form-control'}),
            'primary_author': forms.TextInput(attrs={'class': 'form-control'}),
            'secondary_authors': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }