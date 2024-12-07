from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('driver', 'Driver'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def has_driver_permissions(self):
        return self.user_type == 'driver'

class DriverProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='driver_profile')
    license_number = models.CharField(max_length=50)
    vehicle_details = models.TextField()

    def __str__(self):
        return self.user.username

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    
class HelpRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    help_type = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.help_type}"

class VehicleMedium(models.Model):
    name = models.CharField(max_length=50)  # Car, Bike, Bicycle

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    medium = models.ForeignKey(VehicleMedium, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.medium.name})"
    

class Vehicle(models.Model):
    MEDIUM_CHOICES = (
        ('road', 'Road'),
        ('air', 'Air'),
        ('water', 'Water'),
    )
    name = models.CharField(max_length=100)
    medium = models.CharField(max_length=50, blank=True, null=True)  # Add medium if needed

    def __str__(self):
        return self.name


import datetime
class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings', default=1)  # Set default user ID
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    booking_date = models.DateField(default=datetime.date.today)
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )
