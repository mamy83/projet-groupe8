from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import SolarSystem, Appliance, BatteryReading

class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Adresse Email"
        self.fields['username'].widget = forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'})

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse Email")

    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            del self.fields['username']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

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
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
