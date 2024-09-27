from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Person
from .models import Event
from .models import Venue
from .models import PersonEvent

from django import forms
#for widget:
from django.contrib.admin.widgets import  AdminSplitDateTime
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, SplitDateTimeWidget

#to fix split error:
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class SplitDateTimeField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        # Initialize with date and time fields
        fields = [
            forms.DateField(),
            forms.TimeField()
        ]
        super().__init__(fields, require_all_fields=True, *args, **kwargs)

    def compress(self, data_list):
        # This method combines date and time into one datetime object
        if data_list:
            if data_list[0] is None or data_list[1] is None:
                raise forms.ValidationError("Both date and time are required.")
            return datetime.combine(data_list[0], data_list[1])
        return None

    def to_python(self, value):
        # Expecting a list from the widget; if it’s not a list, raise an error.
        if not isinstance(value, list):
            raise forms.ValidationError(_("Invalid input for date and time."))
        return super().to_python(value)


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
    print("class")
    date = SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        print("meta")
        model = Event
        fields = ['name', 'date', 'description', 'webpage', 'venue', 'persons']  #'__all__'
        #cwidget
        #widgets = {             'date': AdminSplitDateTime(),         }
        # to fix strip error?

    def clean_date(self):
        data = self.cleaned_data.get('date')
        if data is None:
            raise forms.ValidationError("Invalid date and time input.")
        return data

        
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
