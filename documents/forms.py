from django import forms
from .models import Document
from dfrm_admin.models import Employee

class DateInput(forms.DateInput):
    input_type = 'date'

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('title', 'employee_authors', 'publish_date', 'document_type', 'keywords', 'citation', 'file', 'uploaded_by')
        #exclude = ('uploaded_by',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Document Title'}),
            'employee_authors': forms.SelectMultiple(attrs={'class': 'form-select', 'size':10}),
            'publish_date': DateInput(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'form-select', 'size':5}),
            'keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Keywords'}),
            'citation': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Citation'}),
            'file': forms.FileInput(attrs={'class':'form-control'}),
            'uploaded_by': forms.Select(attrs={'class': 'form-select', 'size':5}),
        }