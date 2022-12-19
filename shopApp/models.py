from django.db import models


# Create your models here.
class Room(models.Model):
    numberOfRoom = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=10)
    people_num = models.IntegerField()
    agree = models.BooleanField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
