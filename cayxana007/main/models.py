from django.db import models

# Create your models here.

#menyu modelleri.
from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


#otaq rezervasiyasi.
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")
    reserved_date = models.DateField()
    reserved_time = models.TimeField()
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.room.name} - {self.reserved_date} {self.reserved_time}"





#xususi teklifler.

class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Məsələn, 20.00%
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
