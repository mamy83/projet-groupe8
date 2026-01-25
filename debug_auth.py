import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solarguard.settings')
django.setup()

from django.contrib.auth import authenticate, get_user_model
from core.backends import EmailBackend

User = get_user_model()
email = "ajoseph@gmail.com"
password = "admin123" # I will try to guess/check if this was the password logic, but I can't check password directly.
# The user in step 336 didn't show the password input.

print("--- Debugging ---")
# 1. Check if user exists
try:
    u = User.objects.get(email=email)
    print(f"User found: {u.username} (ID: {u.id})")
    print(f"Email: {u.email}")
    print(f"Password set: {u.has_usable_password()}")
    print(f"Is active: {u.is_active}")
except User.DoesNotExist:
    print(f"User with email {email} NOT FOUND.")
    # Maybe the user created it with a different casing or something?
    all_users = User.objects.all()
    print("Listing all users:")
    for user in all_users:
        print(f"- {user.username} | {user.email}")

# 2. Test Backend Manually
print("\n--- Testing Backend ---")
backend = EmailBackend()
# We don't know the password the user typed in step 336 (it was hidden).
# But we can try to "simulate" it if we knew it.
# Wait, I can't know the password.
# But I can check if the backend logic works for 'admin' which I know the password for ('admin123').

admin_user = User.objects.filter(username='admin').first()
if admin_user:
    print(f"Testing admin auth with email '{admin_user.email}'...")
    # I assume admin email is admin@example.com based on previous steps?
    # Let's check admin email
    print(f"Admin email: {admin_user.email}")
    user_auth = authenticate(username=admin_user.email, password='admin123')
    if user_auth:
        print("SUCCESS: Admin authenticated via email.")
    else:
        print("FAILURE: Admin failed to authenticate via email.")
else:
    print("Admin user not found.")

print("\n--- Testing 'Jose' user ---")
# I cannot test authentication without the password.
# However, if the user "Jose" exists, I can reset his password to something known to test.
