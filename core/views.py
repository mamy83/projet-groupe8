from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SolarSystemForm, ApplianceForm, BatteryReadingForm, CustomUserCreationForm, UserUpdateForm
from .models import SolarSystem, Appliance, BatteryReading
from . import utils

def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/landing.html')

@login_required
def dashboard(request):
    try:
        solar_system = request.user.solar_system
    except SolarSystem.DoesNotExist:
        return redirect('setup_system')
    
    last_reading = BatteryReading.objects.filter(user=request.user).first()
    appliances = Appliance.objects.filter(user=request.user)
    
    # Defaults
    autonomy = None
    recs = {
        'recommended': [],
        'acceptable': [],
        'avoid': []
    }
    
    if last_reading:
        energy_wh = utils.calculate_energy(
            solar_system.battery_capacity_ah, 
            solar_system.system_voltage, 
            last_reading.level_percent
        )
        
        # Simple autonomy estimate based on current appliances average if active?
        essential_load = sum(app.power_w for app in appliances if app.is_essential)
        total_load = sum(app.power_w for app in appliances)
        
        # If no essential appliances, use average of all appliances or 50W default
        avg_load = essential_load or (total_load / (len(appliances) or 1)) or 50
        autonomy = utils.estimate_autonomy(energy_wh, avg_load)
        
        recs = utils.get_recommendations(last_reading.level_percent, appliances)
    
    
    chart_data = utils.get_usage_history(request.user)
    
    context = {
        'solar_system': solar_system,
        'last_reading': last_reading,
        'appliances': appliances,
        'autonomy': autonomy,
        'recommendations': recs,
        'chart_data': chart_data,
    }
    return render(request, 'core/dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend' 
            login(request, user)
            return redirect('setup_system')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def setup_system(request):
    try:
        # Check if system already exists to populate form
        instance = request.user.solar_system
    except SolarSystem.DoesNotExist:
        instance = None

    if request.method == 'POST':
        form = SolarSystemForm(request.POST, instance=instance)
        if form.is_valid():
            solar_system = form.save(commit=False)
            solar_system.user = request.user
            solar_system.save()
            return redirect('dashboard')
    else:
        form = SolarSystemForm(instance=instance)
    return render(request, 'core/setup_system.html', {'form': form})

@login_required
def update_battery(request):
    if request.method == 'POST':
        form = BatteryReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.user = request.user
            reading.save()
            return redirect('dashboard')
    else:
        form = BatteryReadingForm()
    return render(request, 'core/update_battery.html', {'form': form})

@login_required
def add_appliance(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            appliance = form.save(commit=False)
            appliance.user = request.user
            appliance.save()
            return redirect('dashboard')
    else:
        form = ApplianceForm()
    return render(request, 'core/add_appliance.html', {'form': form})

@login_required
def edit_appliance(request, pk):
    appliance = get_object_or_404(Appliance, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ApplianceForm(request.POST, instance=appliance)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ApplianceForm(instance=appliance)
    return render(request, 'core/add_appliance.html', {'form': form})

@login_required
def delete_appliance(request, pk):
    appliance = get_object_or_404(Appliance, pk=pk, user=request.user)
    if request.method == 'POST':
        appliance.delete()
        return redirect('dashboard')
    return render(request, 'core/confirm_delete.html', {'object': appliance})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'core/profile.html', context)
