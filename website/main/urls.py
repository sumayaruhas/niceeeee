from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
  # path('signup/', views.sign_up, name='sign_up'),
    path('', views.help_request_view, name='help_request'),
    path('success/', views.help_success_view, name='help_success'),
    path('signup/driver/', views.driver_sign_up, name='sign_up'),
    path('signup/customer/', views.customer_sign_up, name='customer_signup'),
  # path('login/', views.amiloginkorbo, name='login'),
    path('loginsuggest/', views.suggest_login, name="loginsuggest"),
    path('driver_login/', views.driver_login, name="driver_login"),
    path('customer_login/', views.customer_login, name="customer_login"),
    path('suggest_page/', views.suggest_page, name="suggest_page"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    path('dashboard/driver/', views.driver_dashboard, name='driver_dashboard'),
    path('services/',views.services,name='services'),
    path('registration/car/', views.car_reg, name='car_registration'),
    path('registration/bike/', views.bike_reg, name='bike_registration'),
    path('registration/bicycle/', views.bicycle_reg, name='bicycle_registration'),
    path('help', views.help, name='help'),
    path('deals/', views.deals_list, name='deals'),
    path('deal/<int:deal_id>/claim/', views.click_deal, name='click_deal'),
    path('booking-page/', views.booking_page, name='booking_page'),
    path('booking-form/', views.booking_form, name='booking_form'),
    path('testdashboard/', views.testdashboard, name='testdashboard'),
    path('Driver/Car/Booking/', views.confirm_car_booking, name='confirm_car_booking'),
    path('booking/<int:booking_id>/accept/', views.accept_booking, name='accept_booking'), 
    path('booking/<int:booking_id>/completed/', views.complete_booking, name='complete_booking'), 
    path('testdashboard/', views.testdashboard, name='testdashboard'), 
    path('car-registration-details/', views.car_registration_details, name='car_registration_details'),
    path('update-driver-profile/', views.update_driver_profile, name='update_driver_profile'),
    path('Driver/Car/Pending/', views.pending_car_booking, name='pending_car_booking'),
    path('completed_rides/', views.completed_car_booking, name='completed_rides'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
# cd website
# python manage.py runserver