from django.contrib import admin
from transport.models import Booking, Flight, Location


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
