from django.db import models
from django.utils.translation import gettext_lazy as _  

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(
        "Name of faculty", 
        max_length=300, 
        blank=True, 
        null=True
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Faculties"


class Program(models.Model):
    name = models.CharField(
        "Name of program", 
        max_length=300, 
        blank=True, 
        null=True
    )
    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.CharField(
        max_length=13,
        unique=True,
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
        unique=True, 
        blank=False
    )
    phone_number = models.IntegerField(
        _('phone number'),
        #max_length=10,
        unique=True,
        blank=False
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
