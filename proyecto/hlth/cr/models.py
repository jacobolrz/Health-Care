from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE, null=True,)
    contact_info = models.CharField(max_length=20, blank = True, null = True)
    groups = (
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        )
    user_type = models.CharField(max_length=20, blank = True, null = True, choices = groups)
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
    patient_username = models.CharField(max_length=50)
    weight = models.CharField(max_length=5)
    symptoms = models.CharField(max_length=500)
    prescription = models.CharField(max_length=500)

    def __str__(self):
	    return self.text


class Appointment(models.Model):
    date = models.DateTimeField(default=timezone.now)
    patient_username = models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True)
    weight = models.CharField(max_length=5)
    symptoms = models.CharField(max_length=500)
    prescription = models.CharField(max_length=500)

class Doctor(models.Model):
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    medical_speciality = models.CharField(max_length=50)
    license = models.CharField(max_length=50)

class Patient(models.Model):
    phone_number = models.CharField(max_length=20)
    birthday_year = models.CharField(max_length=4)
    Allergies = models.CharField(max_length=100)



class Profilepage(models.Model):
    user = models.OneToOneField(User, on_delete = models. CASCADE)
    def __str__ (self):
        return f'Perfil de {self.user.username}'

#class Post(models.Model):
#   user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
 #   timestamp = models.DateTimeField(default=timezone.now)
 # 
#  content = models.TextField()

