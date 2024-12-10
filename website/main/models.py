from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
from multiselectfield import MultiSelectField



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
    MEDIUM_CHOICES = (
        ('road', 'Road'),
        ('air', 'Air'),
        ('water', 'Water'),
    )
    name = models.CharField(max_length=100)
    medium = models.CharField(max_length=50, blank=True, null=True)  # Add medium if needed

    def __str__(self):
        return self.name
    

class CarReg(models.Model):
    DISTRICT_CHOICES = [
        ('Dhaka', 'Dhaka'),
        ('Chattogram', 'Chattogram'),
        ('Khulna', 'Khulna'),
        ('Sylhet', 'Sylhet'),
        ('Rajshahi', 'Rajshahi'),
        ('Barishal', 'Barishal'),
        ('Rangpur', 'Rangpur'),
        ('Mymensingh', 'Mymensingh'),
    ]

    COUNTRY_CHOICES = [
        ('Bangladesh', 'Bangladesh'),
    ]

    CITY_CHOICES = [
        ('Dhaka', 'Dhaka'),
        ('Chattogram', 'Chattogram'),
        ('Khulna', 'Khulna'),
        ('Sylhet', 'Sylhet'),
        ('Rajshahi', 'Rajshahi'),
        ('Barishal', 'Barishal'),
        ('Rangpur', 'Rangpur'),
        ('Mymensingh', 'Mymensingh'),
    ]
    

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    district = models.CharField(max_length=100, choices=DISTRICT_CHOICES)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    Transportation = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Car Registration"
        verbose_name_plural = "Car Registrations"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


User = get_user_model()

class Deal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='deal_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DealStatus(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.deal.title} ({self.status})"
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking by {self.name}"
