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

def car_reg(request):
    countries = CarReg.COUNTRY_CHOICES
    districts = CarReg.DISTRICT_CHOICES
    cities = CarReg.CITY_CHOICES
    if request.method == "POST":
        data = request.POST
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phonenumber = request.POST.get('phonenumber')
        district = request.POST.get('district')
        country = request.POST.get('country')
        city = request.POST.get('city')
        transportation = request.POST.get('Transportation') == 'on'  
        
        new_entry = CarReg(
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            district=district,
            country=country,
            city=city,
            Transportation=transportation,
        )
        new_entry.save()
        return redirect ('/registration/car/')
    return render(request, 'car_reg.html',{'countries':countries, 'districts':districts,'cities': cities})

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
    if request.method == 'POST':
        form = DriverSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('driver_dashboard')
    else:
        form = DriverSignUpForm()
    return render(request, 'sign_up.html', {'form': form, 'user_type': 'Driver'})

def driver_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'driver':
            login(request, user)
            return redirect('driver_dashboard')  # Redirect to driver dashboard
        else:
            messages.error(request, "Invalid credentials or not a driver.")
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
