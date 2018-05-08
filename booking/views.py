from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView
from .models import Booking


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking

    queryset = Booking.objects.all()
    context_object_name = 'boo'
    # These next two lines tell the view to index lookups by username
    #fields = ["name", "address", "phone", "position"]
    # slug_field = "booking"
    # slug_url_kwarg = "username"
