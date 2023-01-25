from django.db import models

# Create your models here.

class Hostel(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True
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
        max_length=50,
        blank=True,
        null=True
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
        max_length=50,
        blank=True,
        null=True
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



