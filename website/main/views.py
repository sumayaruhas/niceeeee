from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomerSignUpForm, DriverSignUpForm
from .models import HelpRequest
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Deal, DealStatus
from django.urls import reverse
from .forms import BookingForm
from django.contrib.auth.hashers import *
from django.utils import timezone 

def help_request_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        help_type = request.POST.get('help_type')
        message = request.POST.get('message')

        # Save the data to the database
        HelpRequest.objects.create(name=name, email=email, help_type=help_type, message=message)

        # Redirect to a success page
        return redirect('help_success')
    return render(request, 'help/help.html')

def help_success_view(request):
    return render(request, 'help/help_success.html')

def home(request):
    return render(request, 'home.html')
def sign_up(request):
    return render(request, 'sign_up.html') 

def suggest_page(request):
    return render(request, 'suggest_page.html')

def suggest_login(request):
    return render(request, 'loginsuggest.html')

def services(request):
    return render(request,'Services.html')

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from datetime import datetime
 # Assuming CarReg is a custom model

def car_reg(request):
    if request.method == 'POST':  
        # Extract data from the form
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phonenumber = request.POST.get('phonenumber')
        district = request.POST.get('district')
        country = request.POST.get('country')
        city = request.POST.get('city')
        transportation = request.POST.get('Transportation') == 'on'
        gender = request.POST.get('gender')
        car_brand = request.POST.get('brand')
        car_model = request.POST.get('model')
        reg_area_code = request.POST.get('reg_area_code')
        reg_category = request.POST.get('reg_cat')
        reg_digits = request.POST.get('reg_digits')
        profile_pic = request.FILES.get('profilepic')
        car_pic = request.FILES.get('carpic')
        nid = request.POST.get('nid', '')
        license_no = request.POST.get('license_no')
        selected_date = request.POST.get('selected_date')

        hashed_password=make_password(password)
        # Convert selected date to date object
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date() if selected_date else None

        # Validate mandatory fields
        if not email or not password or not firstname or not lastname or not phonenumber:
            return render(request, 'car_reg.html', {'error': 'All fields are required!'})

        # Create a CarReg instance
        user = CarRegister.objects.create(
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            district=district,
            country=country,
            city=city,
            Transportation=transportation,
            gender=gender,
            brand=car_brand,
            model=car_model,
            reg_area_code=reg_area_code,
            reg_cat=reg_category,
            reg_digits=reg_digits,
            profilepic=profile_pic,
            carpic=car_pic,
            nid=nid,
            email=email,
            license_no=license_no,
            selected_date=selected_date,
            password=hashed_password,
        )
        
        user.reg_no = f"{reg_area_code}{reg_category}{reg_digits}"
        print(firstname, lastname, email, phonenumber, nid)
        # Authenticate and log in the user
        django_user = authenticate(request, username=email, password=password)
        if django_user:
            login(request, django_user)
            user.save()
            return redirect('home') 
        
        return render(request, 'car_reg.html', {'error': 'Authentication failed. Please check your credentials.'})

    # Preload dropdown choices
    params = {
        'countries': CarRegister.COUNTRY_CHOICES,
        'districts': CarRegister.DISTRICT_CHOICES,
        'cities': CarRegister.CITY_CHOICES,
        'genders': CarRegister.GENDER_CHOICES,
        'carbrands': CarRegister.CAR_BRAND,
        'carmodels': CarRegister.CAR_MODEL,
        'regareacode': CarRegister.REG_NO_CODE,
        'regcatehory': CarRegister.REG_NO_CATO,
    }
    return render(request, 'car_reg.html', params)

def bike_reg(request):
    return render(request,'bike_reg.html')

def bicycle_reg(request):
    return render(request,'bicycle_reg.html')

def help(request):
    return render(request,'help.html')

def driver_dashboard(request):
    return render(request, 'driver_dashboard.html')

def customer_sign_up(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = CustomerSignUpForm()
    return render(request, 'customer_sign_up.html', {'form': form, 'user_type': 'Customer'})

def driver_sign_up(request):
    return render(request, 'car_reg.html')

def driver_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        existing_user = CarRegister.objects.filter(email=email).first()
        print('password:' ,password)
        print( check_password(password, existing_user.password))
        if existing_user and check_password(password, existing_user.password):
            request.session['user_id'] = existing_user.id
            existing_user.last_login = timezone.now()
            existing_user.save()
            return redirect('driver_dashboard')  
        return render(request, 'home.html', {'error': "Invalid credentials or not a driver."})
         
    return render(request, 'driver_login.html')

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'customer':
            login(request, user)
            return redirect('customer_dashboard')  # Redirect to customer dashboard
        else:
            messages.error(request, "Invalid credentials or not a customer.")
    return render(request, 'customer_login.html')
  
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def deals_list(request):
    deals = Deal.objects.all()
    return render(request, 'deals.html', {'deals': deals})

@login_required
def click_deal(request, deal_id):
    deal = get_object_or_404(Deal, id=deal_id)
    DealStatus.objects.get_or_create(user=request.user, deal=deal)
    return redirect('customer_dashboard')  # Redirect to the user's dashboard

@login_required
def customer_dashboard(request):
    deal_statuses = DealStatus.objects.filter(user=request.user)
    return render(request, 'customer_dashboard.html', {'deal_statuses': deal_statuses})

def booking_page(request):
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')

        # Store the data in the session or pass it to the form
        request.session['pickup_location'] = pickup_location
        request.session['dropoff_location'] = dropoff_location

        return redirect(reverse('booking_form'))

    return render(request, 'booking_page.html')
from .models import Booking
from django.contrib import messages
from django.shortcuts import redirect, render

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            phone_number = form.cleaned_data['phone_number']
            pickup_location = request.session.get('pickup_location', '')
            dropoff_location = request.session.get('dropoff_location', '')

            # Save booking to the database
            Booking.objects.create(
                name=name,
                age=age,
                phone_number=phone_number,
                pickup_location=pickup_location,
                dropoff_location=dropoff_location
            )

            messages.success(request, 'Booking submitted successfully!')
            return redirect('testdashboard')

    else:
        pickup_location = request.session.get('pickup_location', '')
        dropoff_location = request.session.get('dropoff_location', '')
        form = BookingForm()
    
    return render(request, 'booking_form.html', {
        'form': form,
        'pickup_location': pickup_location,
        'dropoff_location': dropoff_location,
    })
    
def testdashboard(request):
    # Fetch the user's bookings
    user_bookings = Booking.objects.all()  # Filter based on user if you have user accounts

    return render(request, 'testdashboard.html', {'bookings': user_bookings})