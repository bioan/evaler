from django.contrib import admin

# Register your models here.
from api.evaler.models import *

admin.site.register(Event),
admin.site.register(Participant),
