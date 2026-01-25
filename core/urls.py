from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('setup-system/', views.setup_system, name='setup_system'),
    path('update-battery/', views.update_battery, name='update_battery'),
    path('add-appliance/', views.add_appliance, name='add_appliance'),
    path('appliance/<int:pk>/edit/', views.edit_appliance, name='edit_appliance'),
    path('appliance/<int:pk>/delete/', views.delete_appliance, name='delete_appliance'),
    path('profile/', views.profile, name='profile'),
]
