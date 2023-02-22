from django.db import models
from django.contrib.auth.models import User
from master.models import Vehicle
from django.core.validators import RegexValidator


# Create your models here.
class Userdetails(models.Model):
    basic_data = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.TextField(max_length=100)
    Phone_Number = models.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]+$')])
    Date_of_birth = models.DateField()
    Date_of_joining = models.DateField()


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Vehicle_Name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Service_Date = models.DateField()
    Description = models.TextField(max_length=200)
    Reply = models.BooleanField(default=False)


class Breakdown(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Vehicle_Name = models.CharField(max_length=100)
    Place_of_Breakdown = models.CharField(max_length=100)
    Description = models.TextField(max_length=200)
    Status = models.CharField(max_length=200, default="Our Customer care executive will call you soon")
    Reply = models.BooleanField(default=False)


class Feedback(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    feedback = models.TextField(max_length=200)
