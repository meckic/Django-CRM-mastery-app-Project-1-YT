from django.contrib import admin

# Register your models here.

from . models import Person
from . models import Event
from . models import Venue
from . models import PersonEvent
from . models import Feedback


admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(PersonEvent)
admin.site.register(Feedback)



