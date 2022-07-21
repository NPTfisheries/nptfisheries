from django import forms
from .models import Document
from accounts.models import CustomUser

class DocumentForm(forms.ModelForm):
    # uploaded_by = forms.ModelChoiceField(queryset=CustomUser.objects.filter(id=1))

    class Meta:
        model = Document
        fields = ('title', 'primary_author', 'secondary_authors', 'publish_date', 'document_type', 'keywords', 'file', 'uploaded_by',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Document Title'}),
            'primary_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Primary Author'}),
            'secondary_authors': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Secondary Authors'}),
           # 'publish_date': forms.DateField(attrs={'class': 'form-control'}),
            'document_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Type of Document'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Keywords'}),
        }