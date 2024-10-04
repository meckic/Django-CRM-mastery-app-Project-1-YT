from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .forms import CreateUserForm, LoginForm, CreatePersonForm,  UpdatePersonForm, CreateEventForm, UpdateEventForm, CreateVenueForm, UpdateVenueForm, CreateFeedbackForm, UpdateFeedbackForm

from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from .models import Person
from .models import Event
from .models import Venue
#from .models import PersonEvent
from .models import Feedback

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
                return redirect("person-view")
    context = {'form':form}
    return render(request, 'webapp/my-login.html', context=context)

# - Persons
@permission_required('webapp.view_person', raise_exception=True)
def person_view(request):
    my_persons = Person.objects.all()  # .objects.get(pk=book_id) : to get only book with book_id
    context = {'persons': my_persons}
    return render(request, 'webapp/person-view.html', context=context)

# - Events
@permission_required('webapp.view_event', raise_exception=True)
def event_view(request):
    my_events = Event.objects.all()
    context = {'events': my_events}
    return render(request, 'webapp/event-view.html', context=context)

# - Venues
@permission_required('webapp.view_venue', raise_exception=True)
def venue_view(request):
    my_venues = Venue.objects.all()
    context = {'venues': my_venues}
    return render(request, 'webapp/venue-view.html', context=context)

# - Feedback
@permission_required('webapp.view_feedback', raise_exception=True)
def feedback_view(request):
    my_feedback = Feedback.objects.all()
    context = {'feedback': my_feedback}
    return render(request, 'webapp/feedback-view.html', context=context)

# - Create a person 
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
@permission_required('webapp.view_person', raise_exception=True)
def singular_person(request, pk):
    my_person = Person.objects.get(id=pk)
    context = {'person':my_person}
    return render(request, 'webapp/singular-person.html', context=context)

# - Delete a person
@permission_required('webapp.delete_person', raise_exception=True)
def delete_person(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    messages.success(request, "Your person was deleted!")
    return redirect("person-view")


# - Create an event 
@permission_required('webapp.add_event', raise_exception=True)
def create_event(request):
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
           # Save the event or do something with the data
            form.save()
            messages.success(request, "Your event was created!")
            return redirect("event-view")
    context = {'form': form}
    return render(request, 'webapp/create-event.html', context=context)

# - Update an event 
@permission_required('webapp.change_event', raise_exception=True)
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
@permission_required('webapp.view_event', raise_exception=True)
def singular_event(request, pk):
    my_event = Event.objects.get(id=pk)
    context = {'event':my_event}
    return render(request, 'webapp/singular-event.html', context=context)

# - Delete an event
@permission_required('webapp.delete_event', raise_exception=True)
def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    messages.success(request, "Your event was deleted!")
    return redirect("event-view")


# - Create an venue 
@permission_required('webapp.add_venue', raise_exception=True)
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
@permission_required('webapp.change_venue', raise_exception=True)
def update_venue(request, pk):
    venue = Venue.objects.get(id=pk)
    form = UpdateVenueForm(instance=venue)
    if request.method == 'POST':
        form = UpdateVenueForm(request.POST, request.FILES, instance=venue)
        if form.is_valid():
            form.save()
            messages.success(request, "Your venue was updated!")
            return redirect("venue-view")
    context = {'form':form}
    return render(request, 'webapp/update-venue.html', context=context)

# - Read / View a singular venue
@permission_required('webapp.view_venue', raise_exception=True)
def singular_venue(request, pk):
    my_venue = Venue.objects.get(id=pk)
    context = {'venue':my_venue}
    return render(request, 'webapp/singular-venue.html', context=context)

# - Delete an venue
@permission_required('webapp.delete_venue', raise_exception=True)
def delete_venue(request, pk):
    venue = Venue.objects.get(id=pk)
    venue.delete()
    messages.success(request, "Your venue was deleted!")
    return redirect("venue-view")

# - search view
@permission_required('webapp.view_person', raise_exception=True)
def search_view(request):
    query = request.GET.get('search', '')
    print(f'{query = }')
    my_persons = Person.objects.all()
    if query:
        my_persons = my_persons.filter(first_name__icontains=query)
    else:
        my_persons = my_persons.filter(first_name__icontains="xyz") #my_persons empty
    #context = {'count': my_persons.count()}
    context = {'persons': my_persons, 'count': my_persons.count()}
    return render(request, 'webapp/search-view.html', context=context)

# - search results
@permission_required('webapp.view_person', raise_exception=True)
def search_results_view(request):
    query = request.GET.get('search', '')
    print(f'{query = }')
    my_persons = Person.objects.all()
    if query:
        my_persons = my_persons.filter(first_name__icontains=query)
    else:
        my_persons = my_persons.filter(first_name__icontains="xyz") #my_persons empty

    context = {'persons': my_persons, 'count': my_persons.count()}
    return render(request, 'webapp/search-results-view.html', context=context)

# - Create feedback
@permission_required('webapp.add_feedback', raise_exception=True)
def create_feedback(request):
    logged_in_username = request.user.username
    logged_in_useremail = request.user.email
    form = CreateFeedbackForm()
    print("user:", logged_in_username, "email", logged_in_useremail)
    if request.method == "POST":
        form = CreateFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback was created!")
            return redirect("feedback-view")
        else:
            print("FORM ERRORS:", form.errors)
    context = {'form': form}
    return render(request, 'webapp/create-feedback.html', context=context)

# - Read / View a singular feedback
@permission_required('webapp.view_feedback', raise_exception=True)
def singular_feedback(request, pk):
    my_feedback = Feedback.objects.get(id=pk)
    context = {'feedback':my_feedback}
    return render(request, 'webapp/singular-feedback.html', context=context)

# - Update feedback
@permission_required('webapp.change_feedback', raise_exception=True)
def update_feedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    form = UpdateFeedbackForm(instance=feedback)
    if request.method == 'POST':
        form = UpdateFeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback was updated!")
            return redirect("feedback-view")
    context = {'form':form}
    return render(request, 'webapp/update-feedback.html', context=context)

# - Delete a feeback
@permission_required('webapp.delete_feedback', raise_exception=True)
def delete_feedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    feedback.delete()
    messages.success(request, "Your feedback was deleted!")
    return redirect("feedback-view")

# - User logout
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("my-login")




