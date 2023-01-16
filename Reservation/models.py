from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="room_on_floor"
    )
    def __str__(self):
        return self.name

class Block(models.Model):
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
        related_name="floor_on_block"
    ) 
    def __str__(self):
        return self.name


class Hostel(models.Model):
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
        related_name="block_on_hostel"
    )
    def __str__(self):
        return self.name



