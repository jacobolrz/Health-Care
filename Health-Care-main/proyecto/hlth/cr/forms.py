from pyexpat import model
from socket import fromshare
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile
from .models import User
from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_info', 'user_type']    
        labels = {
                "contact_info": _("Contact info"),
                "user_type": _("User type"),
                } 

class AuthenticationUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class Createnewprescription(forms.ModelForm):
    class Meta:
        model = Newprescription
        fields = '__all__'


class DoctorForm(UserCreationForm):
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    medical_speciality = models.CharField(max_length=50)
    license = models.CharField(max_length=50)



class PatientForm(UserCreationForm):
    phone_number = models.CharField(max_length=20)
    birthday_year = models.CharField(max_length=4)
    Allergies = models.CharField(max_length=100)

class CreateAppointment(forms.ModelForm):
    class Meta:
        model = Newprescription
        fields = "__all__"

class UpdateAppointment(forms.ModelForm):
    class Meta:
        model = Newprescription
        fields = "__all__"