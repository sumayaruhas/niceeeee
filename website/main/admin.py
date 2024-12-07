from django.contrib import admin
from .models import CustomUser, DriverProfile, CustomerProfile
from .models import Booking  
from .models import Vehicle

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

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')

    # Optionally customize how 'user' is displayed if needed
    def user(self, obj):
        return obj.user.username  # Display only the username for user field
    user.admin_order_field = 'user'  # Allow ordering by user field
   
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'medium')  # Adjust fields as needed

admin.site.register(Vehicle, VehicleAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'vehicle', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')

admin.site.register(Booking, BookingAdmin)

