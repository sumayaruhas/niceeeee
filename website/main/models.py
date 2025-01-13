from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
from multiselectfield import MultiSelectField
import datetime


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
    

from django.conf import settings
from django.db import models
import datetime

class RiderRegister(models.Model):
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100,default='')
    lastname = models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,null=True, blank=True)
    email = models.EmailField(default='')
    phonenumber = models.CharField(max_length=15, default='')
    password = models.CharField(max_length=255)
    profilepic = models.ImageField( upload_to='profilepic/', null=True, blank=True)
    class Meta:
        verbose_name = "Rider Registration"
        verbose_name_plural = "Riders Registrations"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phonenumber']
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.user.email})"


class CarRegister(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    CAR_BRAND = [
        
        ('BMW','BMW'),
        ('Cherry','Cherry'),
        ('Daihatshu','Daihatsu'),
        ('Ford','Ford'),
        ('Honda','Honda'),
        ('Hyundai','Hyundai'),
        ('Kia','Kia'),
        ('Maruti Suzuki','Maruti Suzuki'),
        ('Mazda','Mazda'),
        ('Mitsubishi','Mitsubishi'),
        ('Nissan','Nissan'),
        ('Proton','Proton'),
        ('Subaru','Subaru'),
        ('Tata','Tata'),
        ('Toyota','Toyota'),
    ]
    CAR_MODEL = [
        ('Accent','Accent'),
        ('Accord','Accord'),
        ('BMW X6','BMW'),
        ('BMW X7','BMW X7'),
        ('BMW 7 Series','BMW 7 Series'),
        ('Civik','Civik'),
        ('Corolla','Corolla'),
        ('Fiesta','Fiesta'),
        ('Elentra','Fiesta'),
        ('Jazz','Jazz'),
        ('Sonata','Fiesta'),


    ]
    REG_NO_CODE = [
        ('DHK METRO','DHK METRO'),
        ('CTG METEO','CTG METEO'),
        ('SYL METRO','SYL METRO'),
        ('KHL METRO','KHL METRO'),
        ('RAJ METRO','RAJ METRO'),
        ('BH','BH'),
        ('BN','BN'),
        ('CH','CH'),
        ('CD','CD'),
        ('CM','CM'),
        ('DH','DH'),
        ('DP','DP'),
        ('FP','FP'),
        ('GB','GB'),
        ('JK','JK'),
    ]
    REG_NO_CATO=[
        ('BHA','BHA'),
        ('CHA','CHA'),
        ('GA','GA'),
        ('GHA','GHA'),
        ('KA','KA'),
        ('KHA','KHA'),
        ('MA','MA'),
        ('PA','PA'),
        ('THA','THA'),
    ]
    
    profilepic = models.ImageField( upload_to='profilepic/', null=True, blank=True)
    carpic = models.ImageField( upload_to='carpic/', null=True, blank=True)
    firstname = models.CharField(max_length=100,default='')
    lastname = models.CharField(max_length=100,default='')
    district = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    Transportation = models.BooleanField(default=False)
    gender = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=100, default='')
    reg_area_code = models.CharField(max_length=100,default='')
    reg_cat = models.CharField(max_length=100,default='9')
    selected_date = models.DateField(default=datetime.date(1999, 10, 10))
    phonenumber = models.CharField(max_length=15, default='')
    license_no = models.CharField(max_length=20, default='')
    reg_digits = models.CharField(max_length=10, default='')
    nid = models.CharField(max_length=20,default='n/a')
    email = models.EmailField(default='')
    reg_no = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255)


    class Meta:
        verbose_name = "Car Driver Registration"
        verbose_name_plural = "Car Driver Registrations"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phonenumber']
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.user.email})"

    def save(self, *args, **kwargs):
        if not self.reg_no:
            self.reg_no = f"{self.reg_area_code}{self.reg_cat}{self.reg_digits}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

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
        ('completed','Completed'),
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
    customerid = models.ForeignKey('RiderRegister', on_delete=models.CASCADE, related_name='customer_bookings',null=True, blank=True)
    driverid = models.ForeignKey('CarRegister', on_delete=models.CASCADE, null=True, blank=True, related_name='driver_bookings')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    pickup_location = models.CharField(max_length=255)
    pickup_date = models.DateField(default=datetime.date(1999, 10, 10))
    pickup_time = models.TimeField(default=datetime.time(0, 0))
    dropoff_location = models.CharField(max_length=255)
    dropoff_date = models.DateField(default=datetime.date(1999, 10, 10))
    dropoff_time = models.TimeField(default=datetime.time(0, 0))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking by {self.name}"
