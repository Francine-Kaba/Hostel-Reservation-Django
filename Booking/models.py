from django.db import models
from django.utils.translation import gettext_lazy as _  
from Authentication.models import Student
from Reservation.models import Room

# Create your models here.

class Booking(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="student"
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="room"
    )
    start_academic_year = models.DateField(
        _('start_academic_year'),
        blank=True,
        null=True,
        auto_now=False, auto_now_add=False, 
        default=0000
    )
    end_academic_year = models.DateField(
        _('end_academic_year'),
        blank=True,
        null=True,
        auto_now=False, auto_now_add=False
    )
    date_booked = models.DateTimeField(
        _('date_booked'),
        blank=True,
        null=True,
        auto_now=False, auto_now_add=False
    )
    price = models.FloatField(
        _('price'),
        max_length=50,
        blank=False,
        null=False,
        default=0.00
    )
    payment = models.BooleanField(
        _('payment'),
        max_length=50,
        blank=False,
        null=False,
        default=False
    )


    def __str__(self):
        return self.student.student_id