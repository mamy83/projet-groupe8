from django.db import models
from django.contrib.auth.models import User

class SolarSystem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='solar_system')
    battery_capacity_ah = models.IntegerField(help_text="Capacité de la batterie en Ah")
    panel_power_w = models.IntegerField(help_text="Puissance des panneaux en Watts")
    system_voltage = models.IntegerField(choices=[(12, '12V'), (24, '24V')], default=12)
    inverter_power_w = models.IntegerField(help_text="Puissance de l'onduleur en Watts", null=True, blank=True)

    def __str__(self):
        return f"Système de {self.user.username}"

class Appliance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appliances')
    name = models.CharField(max_length=100)
    power_w = models.IntegerField(help_text="Consommation en Watts")
    is_essential = models.BooleanField(default=False, help_text="Est-ce un appareil indispensable ?")

    def __str__(self):
        return f"{self.name} ({self.power_w}W)"

class BatteryReading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='readings')
    level_percent = models.IntegerField(help_text="Niveau de batterie en %")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp.strftime('%d/%m %H:%M')} - {self.level_percent}%"
