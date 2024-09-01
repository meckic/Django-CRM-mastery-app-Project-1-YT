from django.contrib import admin

# Register your models here.

from . models import Record
from . models import Event
from . models import Venue

admin.site.register(Record)
admin.site.register(Event)
admin.site.register(Venue)


