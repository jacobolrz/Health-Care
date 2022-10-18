from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile
from .models import User
from .models import *
from django.forms import Textarea



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type']    
        labels = {
                "user_type": _("User type"),
                } 

class AuthenticationUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class Createnewprescription(forms.ModelForm):
    class Meta:
        model = Createprescription
        exclude = ['user']


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
        model = Createprescription
        fields = "__all__"

class UpdateAppointment(forms.ModelForm):
    class Meta:
        model = Createprescription
        fields = "__all__"


class SearchPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Createprescription
        fields = ['patient_username']


class SearchPrescriptionFormPatients(forms.ModelForm):
    class Meta:
        model = Createprescription
        fields = ['user']


class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['user']


class TranslateTextsForm(forms.ModelForm):
    class Meta:
        model = TranslateTexts
        widgets = {'text_to_translate': Textarea(attrs= {'cols': 80, 'rows': 10})}
        fields = ['text_to_translate','language_code_destiny', 'language_code_origin']