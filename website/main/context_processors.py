from .models import *

from django.shortcuts import get_object_or_404

def profile_pic(request):
    if request.user.is_authenticated:
        profile_pic = None

        try:
            if request.user.user_type == 'Driver':
                driver = CarRegister.objects.get(user=request.user)
                profile_pic = driver.profilepic.url if driver.profilepic else 'profilepic/profile.jpg'
            elif request.user.user_type == 'Customer':
                customer = RiderRegister.objects.get(user=request.user)
                profile_pic = customer.profilepic.url if customer.profilepic else 'profilepic/profile.jpg'
        except (CarRegister.DoesNotExist, RiderRegister.DoesNotExist):
            profile_pic = 'profilepic/profile.jpg'  # Default profile picture

        return {'profile_pic': profile_pic}

    return {'profile_pic': 'profilepic/profile.jpg'}
