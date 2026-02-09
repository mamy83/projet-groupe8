from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Adresse Email"
        self.fields['username'].widget = forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'})
