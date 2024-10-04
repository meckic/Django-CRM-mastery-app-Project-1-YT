from django.urls import path

from . import views

urlpatterns = [
#user  
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),

# CRUD
    path('person-view', views.person_view, name="person-view"),
    path('event-view', views.event_view, name="event-view"),
    path('venue-view', views.venue_view, name="venue-view"),
    path('feedback-view', views.feedback_view, name="feedback-view"),
    
    path('create-person', views.create_person, name="create-person"),
    path('update-person/<int:pk>', views.update_person, name='update-person'),
    path('singular-person/<int:pk>', views.singular_person, name="singular-person"),
    path('delete-person/<int:pk>', views.delete_person, name="delete-person"),
    
    path('create-event', views.create_event, name="create-event"),
    path('update-event/<int:pk>', views.update_event, name='update-event'),
    path('singular-event/<int:pk>', views.singular_event, name="singular-event"),
    path('delete-event/<int:pk>', views.delete_event, name="delete-event"),
         
    path('create-venue', views.create_venue, name="create-venue"),
    path('update-venue/<int:pk>', views.update_venue, name='update-venue'),
    path('singular-venue/<int:pk>', views.singular_venue, name="singular-venue"),
    path('delete-venue/<int:pk>', views.delete_venue, name="delete-venue"),

    path('create-feedback', views.create_feedback, name="create-feedback"),
    path('singular-feedback/<int:pk>', views.singular_feedback, name="singular-feedback"),
    path('update-feedback/<int:pk>', views.update_feedback, name='update-feedback'),
    path('delete-feedback/<int:pk>', views.delete_feedback, name="delete-feedback"),

    path('search-view', views.search_view, name='search-view'),
    path('search-results-view', views.search_results_view, name='search-results-view'),

    # nameofwebsubdirANDHtmlFile: .../this-dir    nameofDEFinViews: this_dir     nameof???: this-dir   

]






