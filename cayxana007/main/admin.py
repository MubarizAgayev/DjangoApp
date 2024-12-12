from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MenuCategory, MenuItem, Room, Reservation, SpecialOffer

admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(SpecialOffer)

