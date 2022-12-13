from django.db import models
from django.utils.translation import gettext_lazy as _  

# Create your models here.

class UserRoles(models.Model):     # Model for user role, ie. admin or student 
    name = models.CharField(
        'Name',
        max_length=30,
        blank=False,
        null=False
    )
    def __str__(self):
        return self.name
class Admin(models.Model):        # Model for admin
    first_name = models.CharField(
        _('first name'),
        blank=False,
        null=False
    )
    last_name = models.CharField(
        _('last name'),
        max_length=50,
        blank=False,
        null=False
    )
    email = models.EmailField(
        _('email'),
        unique=True,
        blank=False,
        null=False
    )
    position = models.CharField(
        _('position'),
        max_length=50,
        blank=False,
        null=False
    )
    role= models.ForeignKey(
        UserRoles,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.email

class Faculty(models.Model):        # Model for faculty
    name = models.CharField(
        "Name of faculty", 
        max_length=300, 
        blank=False, 
        null=False
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Faculties"


class Program(models.Model):       # Model for program
    name = models.CharField(
        "Name of program", 
        max_length=300, 
        blank=False, 
        null=False
    )
    def __str__(self):
        return self.name

class Student(models.Model):    # Model for adding a new student
    student_id = models.CharField(
        max_length=13,
        unique=False,
        blank=False,
        null=False
    )
    first_name = models.CharField(
        _('first name'),
        max_length=50,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        _('last name'),
        max_length=50,
        blank=False,
        null=False
    )
    email = models.EmailField(
        _('email address'),
        unique=True, 
        blank=False,
        null=False
    )
    phone_number = models.IntegerField(
        _('phone number'),
        #max_length=10,
        unique=True,
        blank=False,
        null=False
    )
    faculty = models.ForeignKey(
       on_delete=models.CASCADE,
       to="faculty",
       verbose_name = "Faculties"
    )
    program = models.ForeignKey(
       on_delete=models.CASCADE,
       to="program"
    )
    role = models.ForeignKey(
        UserRoles,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.student_id
