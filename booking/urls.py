from django.conf.urls import url
from .views import BookingListView

urlpatterns = [
    url(r'^$', BookingListView.as_view()),
]
