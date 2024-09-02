from django.urls import path

from . import views
#user
urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),

# CRUD
    path('person-view', views.person_view, name="person-view"),
    path('event-view', views.event_view, name="event-view"),
    path('venue-view', views.venue_view, name="venue-view"),
    path('create-person', views.create_person, name="create-person"),
    path('update-person/<int:pk>', views.update_person, name='update-person'),
    path('singular-person/<int:pk>', views.singular_person, name="singular-person"),
    path('delete-person/<int:pk>', views.delete_person, name="delete-person"),
    
    # nameofwebsubdirANDHtmlFile: .../this-dir    nameofDEFinViews: this_dir     nameof???: this-dir   

]






