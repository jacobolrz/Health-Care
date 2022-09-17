from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile
from .forms import CreateUserForm, profileForm
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request): 
    return render(request, 'home.html',{})

def registerPage(request): 
    context = {}
    return render(request, 'register.html', context)

def registerPage(request):  
    form = CreateUserForm()
    profile_form = profileForm()
    context = {'form': form, 'profile_form': profile_form} 
    if request.method == 'POST':
        print(request.POST)
        form = CreateUserForm(request.POST)
        profile_form = profileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            messages.success(request,  'Your account has been successfully created')
            return redirect('login')
    return render(request, 'register.html', context)



def profile (request, username = None ):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)   
    else:
        user = current_user

    return render(request, 'profile.html', {'user':user })




def create_prescription(request):
    data_result = {'form_create_prescription':Createnewprescription}
    if request.method == 'POST':
        formulario = Createnewprescription(request.POST)
        print(request.POST)
        if formulario.is_valid:
            formulario.save()
            data_result['message'] = "Formulario valido"
        else:
            data_result['message'] = "Formulario no valido"
    print(data_result)
    return render(request,'newprescription.html',data_result)