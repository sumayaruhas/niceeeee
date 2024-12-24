from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import CarRegister



class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'customer'
        if commit:
            user.save()
        return user

class DriverSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'driver'
        if commit:
            user.save()
        return user

from .models import HelpRequest

class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['name', 'email', 'help_type', 'message']
        widgets = {
            'help_type': forms.Select(choices=[
                ('General Inquiry', 'General Inquiry'),
                ('Technical Issue', 'Technical Issue'),
                ('Feedback', 'Feedback'),
            ])
        }


from .models import Deal

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title', 'description'] 


import datetime

class BookingForm(forms.Form):
    pickup_date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    pickup_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required=True)
    dropoff_date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    dropoff_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required=True)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CarRegister
        fields = [
            'firstname', 'lastname', 'phonenumber', 'gender', 
            'district', 'country', 'city', 'profilepic', 'carpic',
            'brand', 'model', 'reg_area_code', 'reg_cat', 'reg_digits',
            'license_no', 'nid', 'email'
        ]
        widgets = {
            'gender': forms.Select(choices=CarRegister.GENDER_CHOICES),
            'brand': forms.Select(choices=CarRegister.CAR_BRAND),
            'model': forms.Select(choices=CarRegister.CAR_MODEL),
            'reg_area_code': forms.Select(choices=CarRegister.REG_NO_CODE),
            'reg_cat': forms.Select(choices=CarRegister.REG_NO_CATO),
        }
