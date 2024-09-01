from django.urls import path

from . import views
#user
urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('event-view', views.event_view, name="event-view"),
    path('venue-view', views.venue_view, name="venue-view"),
    path('create-record', views.create_record, name="create-record"),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('record/<int:pk>', views.singular_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    
    # nameofwebsubdirANDHtmlFile: .../this-dir    nameofDEFinViews: this_dir     nameof???: this-dir   

]






