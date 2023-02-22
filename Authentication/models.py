from django.db import models
from django.utils.translation import gettext_lazy as _  
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
# Create your models here.

class UserRole(models.Model):     # Model for user role, ie. admin or student 
    name = models.CharField(
        'Name',
        max_length=30,
        blank=False,
        null=False
    )
    def __str__(self):
        return self.name

class Position(models.Model):       # Model for position
    name = models.CharField(
        "Name of position", 
        max_length=300, 
        default='Student'
    )
    def __str__(self):
        return self.name

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
        
class User(AbstractBaseUser):        # Model for admin
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
        _('email'),
        unique=True,
        blank=False,
        null=False
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    role = models.ForeignKey(
        UserRole,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(
        _('phone_number'),
        max_length=20,
        blank=True,
        null=True
    )
    is_admin = models.BooleanField(
        _('is_admin'),
         default=False
    )
    is_superuser = models.BooleanField(
        _('is_superuser'),
         default=False
    )
    is_staff = models.BooleanField(
        _('is_staff'),
         default=False
    )
    def __str__(self):
        return self.email

    objects = UserManager()
    USERNAME_FIELD = 'email'


class Student(models.Model):    # Model for adding a new student
    student_id = models.CharField(
        max_length=13,
        unique=True,
        blank=False,
        null=False
    )
    user = models.ForeignKey(
       on_delete=models.CASCADE,
       to="User"
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
    def __str__(self):
        return self.student_id

   