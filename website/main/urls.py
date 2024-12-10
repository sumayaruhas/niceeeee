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
    path('registration/bicycle/', views.car_reg, name='bicycle_registration'),
    path('help', views.help, name='help'),
   path('deals/', views.deals_list, name='deals'),
    path('deal/<int:deal_id>/claim/', views.click_deal, name='click_deal'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# cd website
# python manage.py runserver