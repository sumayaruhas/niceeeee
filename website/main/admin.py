from django.contrib import admin
from .models import *
from .models import Deal, DealStatus
from .models import Booking


# import the Booking model

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_active')

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number')

    # Custom queryset to show only drivers
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(user__user_type='driver')

@admin.register(RiderRegister)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['email','firstname', 'lastname' , 'phonenumber', 'gender', 'profilepic']

    search_fields = ['firstname', 'lastname', 'email']

    fieldsets = (
    (None, {
        'fields': ('firstname', 'lastname', 'email', 'phonenumber', 'gender')
    }),
    ('Profile Information', {
        'fields': ('profilepic',)
    }),
    )
    list_filter = ['gender']  # Allow ordering by user field

@admin.register(CarRegister)
class CarRegAdmin(admin.ModelAdmin):
    list_display = ['email','firstname', 'lastname' , 'phonenumber', 'gender', 'brand', 'model', 'license_no', 'nid', 'profilepic', 'carpic', 'selected_date']

    search_fields = ['firstname', 'lastname', 'email', 'license_no', 'nid']

    fieldsets = (
    (None, {
        'fields': ('firstname', 'lastname', 'email', 'phonenumber', 'gender')
    }),
    ('Car Details', {
        'fields': ('brand', 'model', 'reg_area_code', 'reg_cat', 'license_no', 'reg_digits', 'selected_date', 'carpic')
    }),
    ('Address Information', {
        'fields': ('district', 'country', 'city')
    }),
    ('Profile Information', {
        'fields': ('profilepic',)
    }),
    ('Other Info', {
        'fields': ('nid', 'Transportation')
    }),
    )
    list_filter = ['gender', 'Transportation', 'country', 'city']

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'image']

@admin.register(DealStatus)
class DealStatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'deal', 'status']



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'pickup_location', 'dropoff_location', 'status')
    list_filter = ('status',)
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(status='approved')  # Update the 'status' field
        self.message_user(request, "Selected bookings have been approved.")  # Optional success message

    approve_bookings.short_description = "Approve selected bookings"
