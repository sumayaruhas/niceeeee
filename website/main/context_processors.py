from .models import *

from django.shortcuts import get_object_or_404

def profile_pic(request):
    if request.user.is_authenticated:
        try:
            
            rider = CarRegister.objects.get(user=request.user)
            
            return {'profile_pic': rider.profilepic.url if rider.profilepic else 'profilepic/profile.jpg'}
        except CarRegister.DoesNotExist:
            
            return {'profile_pic': 'profilepic/profile.jpg'}
    return {'profile_pic': None}
