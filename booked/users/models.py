from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

POSITION = (('Faculty', 'Faculty'),
            ('Staff', 'Staff'),
            ('Driver', 'Driver'),
            )


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), max_length=255)
    address = models.CharField(_("Address"), max_length=255, default='')
    phone = models.CharField(_("Phone"), max_length=100, default='')
    position = models.CharField(choices=POSITION, max_length=10, default='Faculty')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
