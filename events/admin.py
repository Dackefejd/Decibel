from django.contrib import admin
from .models import *

apps = [EventCategory, EventType, Genre, Location, Event]


admin.site.register(apps)