from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from user.models import Userdetails, Service, Breakdown, Feedback


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class Registrationform(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = ('Address', 'Phone_Number', 'Date_of_birth', 'Date_of_joining')
        widgets = {
            'Date_of_birth': DateInput(),
            'Date_of_joining': DateInput(),
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class Serviceform(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['Vehicle_Name', 'Service_Date', 'Description']
        widgets = {
            'Service_Date': DateInput(),
        }


class Breakdownform(forms.ModelForm):
    class Meta:
        model = Breakdown
        fields = ['Vehicle_Name', 'Place_of_Breakdown', 'Description']


class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['Name', 'Email', 'feedback']