from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError

class GuestForm(forms.Form):
    email = forms.EmailField(widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                
                'placeholder' : 'Username'
            }))


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'}))


class RegisterForm(forms.Form):

    username = forms.CharField(widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'style': 'width: 400px',
                'placeholder' : 'Username'
            }
        ))
    email    = forms.EmailField(widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'style': 'width: 400px',
                'placeholder' : 'Email'
            }))
    password = forms.CharField(widget=forms.PasswordInput( 
        attrs={
                'class' : 'form-control',
                'style': 'width: 400px',
                'placeholder' : 'Passoword'
            }))
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput( 
        attrs={
                'class' : 'form-control',
                'style': 'width: 400px',
                'placeholder' : 'Confirm Passoword'

            }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean_password2(self):

        data = self.cleaned_data
        password=self.cleaned_data.get("password")

        password2 = self.cleaned_data.get("password2")
        print(password,password2)

        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data
