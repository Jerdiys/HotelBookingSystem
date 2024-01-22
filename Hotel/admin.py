from django.contrib import admin
from .models import Room, RoomBooking

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomtype', 'roomprice', 'roomphoto')

admin.site.register(Room, RoomAdmin)

class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'roomtype', 'check_in_date', 'check_out_date', 'booking_code')

admin.site.register(RoomBooking, RoomBookingAdmin)
