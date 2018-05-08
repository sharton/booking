from django.db import models
from booked.users.models import User


class Route(models.Model):
    route_name = models.CharField(max_length=200, help_text="Name of the route")
    route_desc = models.TextField()

    def __str__(self):
        return self.route_name


# class Car(models.Model):
#     car_name = models.CharField(max_length=200, help_text="Name of the route")
#     quantity_places = models.IntegerField()
#     driver = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.driver + "-" + self.car_name


class Trip(models.Model):

    DAYS = (('ПН', 'MON'),
            ('ВТ', 'TUE'),
            ('СР', 'WED'),
            ('ВТ', 'TUE'),
            ('СР', 'WED'),
            ('ЧТ', 'THU'),
            ('ПТ', 'FRI'),
            )

    day_trip = models.CharField(choices=DAYS, max_length=10, default='MON')
    time_trip = models.TimeField()
    # car = models.ForeignKey(Car, on_delete=None)
    route = models.ForeignKey(Route, on_delete=None)

    @property
    def trip(self):
        return self.route.route_name + "-" + str(self.time_trip)

    def __str__(self):
        return self.route.route_name + "-" + str(self.time_trip)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=None)
    trip = models.ForeignKey(Trip, on_delete=None)

    def __str__(self):
        return self.user.name + "-"+ str(self.trip.time_trip) + "-" + self.trip.route.route_name
