from django.contrib import admin
from .models import Booking, Route, Trip



# Register your models here.
admin.site.register(Route)
admin.site.register(Trip)


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    # fieldsets = (("User Profile", {"fields": ("name",)}),) + AuthUserAdmin.fieldsets
    list_display = ("user", "trip")
    search_fields = ["user"]
