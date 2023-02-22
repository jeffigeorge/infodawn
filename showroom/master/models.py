from django.db import models


# Create your models here.

class Vehicle(models.Model):
    Vehicle_Name = models.CharField(max_length=100)
    Vehicle_Type = models.CharField(max_length=100)
    Description = models.TextField(max_length=300)
    Vehicle_Color = models.CharField(max_length=100)
    Rate = models.IntegerField()
    TRate = models.IntegerField(default=100)
    Weight = models.CharField(max_length=100)
    Capacity = models.CharField(max_length=100)
    Mileage = models.CharField(max_length=100)
    Fuel = models.CharField(max_length=100)
    Vehicle_Model = models.CharField(max_length=100)
    Year_of_built = models.CharField(max_length=100)
    Autogear = models.CharField(max_length=100)
    Seatcap = models.CharField(max_length=100)
    Center_lock = models.CharField(max_length=100)
    Power_steering = models.CharField(max_length=100)
    Power_break = models.CharField(max_length=100)
    Tyre = models.CharField(max_length=100)
    Chassis = models.CharField(max_length=100)
    Vehicle_Image = models.ImageField(upload_to='media/images')

    def save(self, *args, **kwargs):
        try:
            self.TRate = (self.Rate/10)*100
        except TypeError:
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Vehicle_Name


class Accessories(models.Model):
    Accessory_Name = models.CharField(max_length=100)
    Vehicle_Name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Description = models.TextField(max_length=300)
    Rate = models.IntegerField()
    TRate = models.IntegerField(default=100)
    Accessory_Image = models.ImageField(upload_to='media/images')

    def save(self, *args, **kwargs):
        try:
            self.TRate = self.Rate * 100
        except TypeError:
            pass
        super().save(*args, **kwargs)
