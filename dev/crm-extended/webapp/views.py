from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .forms import CreateUserForm, LoginForm, CreatePersonForm,  UpdatePersonForm, CreateEventForm, UpdateEventForm, CreateVenueForm, UpdateVenueForm

from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from .models import Person
from .models import Event
from .models import Venue

#from django.middleware.common import MiddlewareMixin
#from django.http import HttpResponse
#import logging
#logger = logging.getLogger(__name__)
#class GlobalExceptionHandlerMiddleware(MiddlewareMixin):
#    def process_exception(self, request, exception):
        #logger.exception(f"An error occurred: {exception}")
        ## Render a custom error template
        #return render(request, 'errors/500.html', {'exception': exception})
#        messages.error( "You are not authorized!")

#def handle_exception(request, exception):
#    if isinstance(exception, PermissionDenied):
#        messages.error(request, "You are not authorized!")
#        return render(request, 'permission_denied.html')
#    return None

# - Homepage 
def home(request):
    return render(request, 'webapp/index.html')

#def error(request):
#    return render(request, 'webapp/error.html')


# - Register a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("my-login")
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)

# - Login a user
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("person-view")
    context = {'form':form}
    return render(request, 'webapp/my-login.html', context=context)

# - Persons
@login_required(login_url='my-login')
def person_view(request):
    my_persons = Person.objects.all()
    context = {'persons': my_persons}
    return render(request, 'webapp/person-view.html', context=context)

# - Events
@login_required(login_url='my-login')
def event_view(request):
    my_events = Event.objects.all()
    context = {'events': my_events}
    return render(request, 'webapp/event-view.html', context=context)

# - Venues
@login_required(login_url='my-login')
def venue_view(request):
    my_venues = Venue.objects.all()
    context = {'venues': my_venues}
    return render(request, 'webapp/venue-view.html', context=context)


# - Create a person 
#@login_required(login_url='my-login')
@permission_required('webapp.add_person', raise_exception=True)
def create_person(request):
    form = CreatePersonForm()
    if request.method == "POST":
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your person was created!")
            return redirect("person-view")
    context = {'form': form}
    return render(request, 'webapp/create-person.html', context=context)

# - Update a person 
#@login_required(login_url='my-login')
@permission_required('webapp.change_person', raise_exception=True)
def update_person(request, pk):
    person = Person.objects.get(id=pk)
    form = UpdatePersonForm(instance=person)
    if request.method == 'POST':
        form = UpdatePersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, "Your person was updated!")
            return redirect("person-view")
    context = {'form':form}
    return render(request, 'webapp/update-person.html', context=context)

# - Read / View a singular person
#@login_required(login_url='my-login')
@permission_required('webapp.view_person', raise_exception=True)
def singular_person(request, pk):
    my_person = Person.objects.get(id=pk)
    context = {'person':my_person}
    return render(request, 'webapp/singular-person.html', context=context)

# - Delete a person
#@login_required(login_url='my-login')
@permission_required('webapp.delete_person', raise_exception=True)
def delete_person(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    messages.success(request, "Your person was deleted!")
    return redirect("person-view")


# - Create an event 
@login_required(login_url='my-login')
def create_event(request):
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your event was created!")
            return redirect("event-view")
    context = {'form': form}
    return render(request, 'webapp/create-event.html', context=context)

# - Update an event 
@login_required(login_url='my-login')
def update_event(request, pk):
    event = Event.objects.get(id=pk)
    form = UpdateEventForm(instance=event)
    if request.method == 'POST':
        form = UpdateEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Your event was updated!")
            return redirect("event-view")
    context = {'form':form}
    return render(request, 'webapp/update-event.html', context=context)

# - Read / View a singular event
@login_required(login_url='my-login')
def singular_event(request, pk):
    my_event = Event.objects.get(id=pk)
    context = {'event':my_event}
    return render(request, 'webapp/singular-event.html', context=context)

# - Delete an event
@login_required(login_url='my-login')
def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    Event.delete()
    messages.success(request, "Your event was deleted!")
    return redirect("event-view")


# - Create an venue 
@login_required(login_url='my-login')
def create_venue(request):
    form = CreateVenueForm()
    if request.method == "POST":
        form = CreateVenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your venue was created!")
            return redirect("venue-view")
    context = {'form': form}
    return render(request, 'webapp/create-venue.html', context=context)

# - Update an venue 
@login_required(login_url='my-login')
def update_venue(request, pk):
    venue = Venue.objects.get(id=pk)
    form = UpdateVenueForm(instance=venue)
    if request.method == 'POST':
        form = UpdateVenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            messages.success(request, "Your venue was updated!")
            return redirect("venue-view")
    context = {'form':form}
    return render(request, 'webapp/update-venue.html', context=context)

# - Read / View a singular venue
@login_required(login_url='my-login')
def singular_venue(request, pk):
    my_venue = Venue.objects.get(id=pk)
    context = {'venue':my_venue}
    return render(request, 'webapp/singular-venue.html', context=context)

# - Delete an venue
@login_required(login_url='my-login')
def delete_venue(request, pk):
    venue = Venue.objects.get(id=pk)
    Venue.delete()
    messages.success(request, "Your venue was deleted!")
    return redirect("venue-view")


# - User logout
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("my-login")




