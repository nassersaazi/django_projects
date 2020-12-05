from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    docstring
    """
    email = forms.EmailField(required=True)
    # phone = forms.CharField(required=True)
    # area = forms.CharField(required=True)

    class Meta():
        """
        docstring
        """
        model = User
        fields = [
            'username',
            'email',
            # 'area',
            # 'phone',
            'password1',
            'password2'
        ]
   
    


