from django.contrib import admin
from .models import Airport, Flight, Pessenger
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Pessenger)
