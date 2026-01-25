from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SolarSystem, Appliance, BatteryReading

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse Email")

    class Meta:
        model = User
        fields = ("username", "email")

class SolarSystemForm(forms.ModelForm):
    class Meta:
        model = SolarSystem
        fields = ['battery_capacity_ah', 'panel_power_w', 'system_voltage', 'inverter_power_w']
        labels = {
            'battery_capacity_ah': 'Capacité Batterie (Ah)',
            'panel_power_w': 'Puissance Panneaux (W)',
            'system_voltage': 'Tension Système',
            'inverter_power_w': 'Puissance Onduleur (W)',
        }

class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = ['name', 'power_w', 'is_essential']
        labels = {
            'name': 'Nom de l\'appareil',
            'power_w': 'Puissance (Watts)',
            'is_essential': 'Essentiel ?',
        }

class BatteryReadingForm(forms.ModelForm):
    class Meta:
        model = BatteryReading
        fields = ['level_percent']
        labels = {
            'level_percent': 'Niveau de batterie (%)',
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Adresse Email")

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Nom d\'utilisateur',
        }
