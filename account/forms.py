from django import forms
from django.forms import TextInput, EmailInput, PasswordInput, FileInput


class ProfileForm(forms.Form):  
    username = forms.CharField(label="Enter username",max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    email  = forms.EmailField(label="Enter email", widget=forms.EmailInput(attrs={'class': 'form-control'}))  
    password = forms.CharField(label="Enter password",max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repassword = forms.CharField(label="Confirm your password",max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    image = forms.FileField(widget= forms.FileInput(attrs={
        'class':'imagecrop',
        'accept':'image/jpeg,image/png,image/gif'}))