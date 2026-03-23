from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, label="Username")
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm password")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=False, label="Title", widget=forms.TextInput(attrs={'placeholder': 'Optional title'}))
    caption = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your memory...'}), required=True, label="Caption")

    class Meta:
        model = Post
        fields = ['title', 'caption']
