from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book
from .models import Author
from .models import BookAuthor

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# - Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - Create a book

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']

class CreateBookAuthorForm(forms.ModelForm):
    class Meta:
        model = BookAuthor
        fields = ['book', 'author', 'role']


class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']

class UpdateBookAuthorForm(forms.ModelForm):
    class Meta:
        model = BookAuthor
        fields = ['book', 'author', 'role']
