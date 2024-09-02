from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreatePersonForm, UpdatePersonForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Person
from .models import Event
from .models import Venue

from django.contrib import messages

# - Homepage 
def home(request):
    return render(request, 'webapp/index.html')

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
                return redirect("dashboard")
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
@login_required(login_url='my-login')
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
@login_required(login_url='my-login')
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
@login_required(login_url='my-login')
def singular_person(request, pk):
    my_person = Person.objects.get(id=pk)
    context = {'person':my_person}
    return render(request, 'webapp/singular-person.html', context=context)

# - Delete a person
@login_required(login_url='my-login')
def delete_person(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    messages.success(request, "Your person was deleted!")
    return redirect("person-view")

# - User logout
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("my-login")




