from django.contrib import admin
from .models import SolarSystem, Appliance, BatteryReading

admin.site.register(SolarSystem)
admin.site.register(Appliance)
admin.site.register(BatteryReading)
