# accounts/forms.py
from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser, UserProfile

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('affiliation', 'work_phone', 'mobile_phone', 'email_updates', 'city', 'state', 'bio', 'profile_picture')

        widgets = {
            'affiliation': forms.Select(attrs={'class': 'form-control', 'placeholder':'Nez Perce Tribe'}),
            'work_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_updates': forms.CheckboxInput(attrs={'class': 'form-check form'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lapwai'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Idaho'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Biography'}),
            'profile_picture': forms.FileInput(attrs={'class':'form-control'}),
        }
