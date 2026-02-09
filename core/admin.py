from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, UserUpdateForm
from .models import SolarSystem, Appliance, BatteryReading

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserUpdateForm
    model = User
    list_display = ["email", "is_staff", "is_active"]
    list_filter = ["email", "is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email",),
        }),
    )
    search_fields = ["email"]
    ordering = ["email"]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(SolarSystem)
admin.site.register(Appliance)
admin.site.register(BatteryReading)
