from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"DEBUG: EmailBackend.authenticate handling user: '{username}'")
        UserModel = get_user_model()
        try:
            # Try to fetch the user by username or email
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            print(f"DEBUG: User found: {user.username} (email: {user.email})")
        except UserModel.DoesNotExist:
            print("DEBUG: User not found/DoesNotExist")
            return None
        except UserModel.MultipleObjectsReturned:
            # If multiple users have the same email (shouldn't happen with unique constraint, but safe fallback)
            user = UserModel.objects.filter(email__iexact=username).order_by('id').first()
            print(f"DEBUG: Multiple objects returned, using: {user.username}")

        if user.check_password(password) and self.user_can_authenticate(user):
            print("DEBUG: Password correct. Authentication successful.")
            return user
        
        print(f"DEBUG: Authentication failed. user.check_password: {user.check_password(password)}")
        return None
