from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Register/create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','password1','password2']

# login user
 
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


#create record form
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record

        fields = ['first_name','last_name','email','phone','address','city','province','country']

# - Update a record form
class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record

        fields = ['first_name','last_name','email','phone','address','city','province','country']

