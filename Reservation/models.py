from django.db import models
from django.utils.translation import gettext_lazy as _  

# Create your models here.

class Hostel(models.Model):
    name = models.CharField(
        "Name of hostel", 
        max_length=300, 
        blank=False, 
        null=False
    )
    hostel_type = models.CharField(
        _('hostel type'),
        max_length=50,
        blank=False,
        null=False,
        default="Campus Hostel"
    )
    contact = models.CharField(
        _('contact'),
        max_length=20,
        blank=True,
        null=True
    )
    hostel_image = models.ImageField(
        _('hostel image'),
        upload_to='hostel_images/',
        blank=False,
        null=False
    )
    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(
        "Name of block", 
        max_length=300, 
        blank=False, 
        null=False
    )
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="hostel_in_school"
    )
    def __str__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(
        "Name of floor", 
        max_length=300, 
        blank=False, 
        null=False
    )
    gender = models.CharField(
        _('gender'),
        max_length=50,
        blank=False,
        null=False,
        default="Mixed"
    )
    block = models.ForeignKey(
        Block,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="block_in_hostel"
    ) 
    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(
        "Name of room", 
        max_length=300, 
        blank=False, 
        null=False
    )
    number_of_persons = models.IntegerField(
        _('number of persons'),
        blank=False,
        null=False,
        default=0
    )
    is_available = models.CharField(
        _('is available'),
        max_length=50,
        blank=False,
        null=False,
        default=False
    )
    price = models.FloatField(
        _('price'),
        max_length=50,
        blank=False,
        null=False,
        default=0.00
    )
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="floor_in_block"
    )
    
    objects = models.Manager()

    def __str__(self):
        return self.name



