from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Person
from .models import Event
from .models import Venue
from .models import PersonEvent

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

# - Create a person
class CreatePersonForm(forms.ModelForm):    # do NOT ment. the autocreated
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country', 'events']
        
# - Update a person
class UpdatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__' #['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country', 'events']

# - Create an event
class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__' #['name', 'date', 'description', 'webpage', 'venue', 'persons']  
       
# - Update an event
class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__' #['name', 'date', 'description', 'webpage', 'venue', 'persons']

# - Create an venue
class CreateVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'email', 'phone', 'address', 'city', 'province', 'country', 'upload']
        
# - Update an venue
class UpdateVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'email', 'phone', 'address', 'city', 'province', 'country', 'upload']

# - PersonEvent
class PersonEventForm(forms.ModelForm):
    class Meta:
        model = PersonEvent
        fields = '__all__' 
