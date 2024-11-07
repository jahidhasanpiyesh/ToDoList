from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import add_post

class loginforms(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class userforms(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmation Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email',]
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
        
class add_post_forms(forms.ModelForm):
    class Meta:
        model = add_post
        fields = ['title','desh']
        labels = {'title':'Title', 'desh':'Description'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desh':forms.Textarea(attrs={'class':'form-control'})
        }