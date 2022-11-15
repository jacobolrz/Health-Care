from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE, null=True,)
    groups = (
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        )
    user_type = models.CharField(max_length=20, blank = False, null = False, choices = groups)
    def __str__(self):
        return self.name


class Prescriptions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prescriptions", null=True) 
    last_name = models.CharField(max_length=200)

    def __str__(self):
	    return self.name

class Newprescription(models.Model):
    prescription = models.ForeignKey(Prescriptions, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    patient_username = models.CharField(max_length=50)
    weight = models.CharField(max_length=5)
    symptoms = models.CharField(max_length=500)
    prescription = models.CharField(max_length=500)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
	    return self.text

class Createprescription(models.Model):
    prescription = models.ForeignKey(Prescriptions, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    patient_username = models.CharField(max_length=50)
    weight = models.IntegerField()
    symptoms = models.CharField(max_length=500)
    prescription = models.CharField(max_length=500)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
	    return self.text


class Appointment(models.Model):
    date = models.DateTimeField(default=timezone.now)
    patient_username = models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True)
    weight = models.CharField(max_length=5)
    symptoms = models.CharField(max_length=500)
    prescription = models.CharField(max_length=500)

class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=100)
    medical_speciality = models.CharField(max_length=50)
    license = models.CharField(max_length=50)

class Patient(models.Model):
    birthday_year = models.CharField(max_length=4)
    Allergies = models.CharField(max_length=100)

class Costumer(models.Model):
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    medical_speciality = models.CharField(max_length=50)
    license = models.CharField(max_length=50)

class TranslateTexts(models.Model):
    TYPE_LANGUAGE_CHOICE = [('en', 'english'), ('fr', 'french'), ('de', 'deutch'),('it', 'italian'), ('es', 'spanish')]
    TYPE_LANGUAGE = [('en', 'english'), ('fr', 'french'), ('de', 'deutch'),('it', 'italian'), ('es', 'spanish') ]
    language_code_origin = models.CharField(max_length=2, choices=TYPE_LANGUAGE)
    language_code_destiny = models.CharField(max_length=2, choices=TYPE_LANGUAGE_CHOICE)
    text_to_translate = models.CharField(max_length=255)
    text_translated = models.CharField(max_length=255)

    def _str_ (self):
        return 'el texto traducido es %s %s' % (self.language_code_destiny, self.text_translated)


class Profilepage(models.Model):
    user = models.OneToOneField(User, on_delete = models. CASCADE)
    def __str__ (self):
        return f'Perfil de {self.user.username}'

# Create your models here.
