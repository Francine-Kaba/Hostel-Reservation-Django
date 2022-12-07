from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(models.Model):
    username = models.CharField(
        max_length=300,
        blank=False
    )
    first_name = models.CharField(
        _('first name'),
        max_length=50,
        blank=False
    )
    last_name = models.CharField(
        _('last name'),
        max_length=50,
        blank=False
    )
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    phone_number = models.IntegerField(
        _('phone number'),
        max_length=10,
        unique=True,
        blank=True
    )
    username = models.CharField(
        _('username'),
        blank=False
    )
    def __str__(self):
        return self.name
