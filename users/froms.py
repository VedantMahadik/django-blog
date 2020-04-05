from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # to add some fields in form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Images are in profile so cant be used in UserUpdateForm
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']        