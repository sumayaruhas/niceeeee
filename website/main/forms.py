from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Booking, VehicleMedium

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

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_location', 'dropoff_location', 'date', 'time', 'vehicle']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    vehicle = forms.ModelChoiceField(queryset=VehicleMedium.objects.all(), empty_label="-- Select Vehicle --", required=True)
