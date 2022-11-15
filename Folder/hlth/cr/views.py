from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from .forms import CreateUserForm, profileForm
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.db.models import F
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from itertools import count
from django.shortcuts import render
import requests, uuid, json
from .forms import * 
from .models import *
from django.contrib.auth.decorators import login_required
import requests, uuid, json

# Create your views here.


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


@login_required
def profile (request, username = None ):
    user = request.user 
    doctor = Profile.objects.all
    user_request = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user = user_request)
    prescription = Createprescription.objects.filter(deleted_date__isnull=True, user = user )
    prescription_patients = Createprescription.objects.filter(deleted_date__isnull=True, patient_username = user )
    data_context = {'user_data' : user_request, 'user_profile' : user_profile,  'prescription_list': prescription, 'prescription_list_patients': prescription_patients }
    
    return render (request, 'profile.html', data_context )

        
    return render(request,'profile.html',data_context)

def create_doctor(request):
    data_result = {'form_create_doctor':CreateDoctorForm}
    if request.method == 'POST':
        formulario = CreateDoctorForm(request.POST)
        formulario.user = request.user
        print(request.POST)
        if formulario.is_valid:
            instance = formulario. save(commit=False)
            instance.user = request.user
            instance.save()
            data_result['message'] = "Formulario valido"
        else:
            data_result['message'] = "Formulario no valido"
    print(data_result)
    return render(request,'profile.html',data_result)

@login_required
def create_prescription(request):
    data_result = {'form_create_prescription':Createnewprescription}
    if request.method == 'POST':
        formulario = Createnewprescription(request.POST)
        formulario.user = request.user
        print(request.POST)
        if formulario.is_valid:
            instance = formulario. save(commit=False)
            instance.user = request.user
            instance.save()
            data_result['message'] = "Formulario valido"
            return redirect('profile')
        else:
            data_result['message'] = "Formulario no valido"
    print(data_result)
    return render(request,'newprescription.html',data_result)

@login_required
def doctor_information(request):
    data_result = {'form_doctor_information':CreateDoctorForm}
    if request.method == 'POST':
        formulario = CreateDoctorForm(request.POST)
        formulario.user = request.user
        print(request.POST)
        if formulario.is_valid:
            instance = formulario. save(commit=False)
            instance.user = request.user
            instance.save()
            data_result['message'] = "Formulario valido"
        else:
            data_result['message'] = "Formulario no valido"
    print(data_result)
    return render(request,'doctor.html',data_result)

@login_required
def view_prescription_list(request):
    user = request.user
    prescription = Createprescription.objects.filter(deleted_date__isnull=True, user = user  )
    data_result = {'prescription_list': prescription}
    return render (request, 'myprescriptions.html', data_result )

@login_required
def view_prescription_list_patients(request):
    current_user = request.user
    prescription_patients = Createprescription.objects.filter(deleted_date__isnull=True, patient_username = current_user  )
    data_result = {'prescription_list_patients': prescription_patients}
    return render (request, 'myprescriptionspatients.html', data_result )

@login_required
def search_prescription(request):
    user = request.user
    prescriptionsearch_form = SearchPrescriptionForm() 
    data_context = {'prescriptionsearch_form': prescriptionsearch_form}
    data_context['empty_search'] = True
    if request.method == 'POST':
        prescriptionsearch_form = SearchPrescriptionForm(request.POST) 
        if prescriptionsearch_form.is_valid():
            prescription_list = Createprescription.objects.filter(patient_username__contains=request.POST.get('patient_username')).filter(deleted_date__isnull=True )
            data_context['prescription_list'] = prescription_list
            data_context['empty_search'] = False
    
    return render(request,'search_prescription.html',data_context)



@login_required
def translate (request, createprescription_id):
    translateform = TranslateTextsForm()
    newprescription = Createprescription.objects.get(pk=createprescription_id)
    context = {'translateform':translateform, 'newprescription': newprescription}

    if request.method == 'POST':

        translateform = TranslateTextsForm(request.POST)
        print(request.POST)
        print(request.POST.get('language_code_origin'))
        print(request.POST.get('language_code_destiny'))

        # Add your key and endpoint
        key = "30bb7b15b98742389f3b2397f59218e6"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "eastus"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from':  [request.POST.get('language_code_origin')],
            'to': [request.POST.get('language_code_destiny')]
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4()),
            'Ocp-Apim-Subscription-Region': location
        }

        # You can pass more than one object in body.
        body = [{
            'text': newprescription.symptoms
        }]

        translate = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = translate.json()
        z = response [0]
        a= z ['translations']
        a[0]
        y= a[0]
        response = y ['text']

        context['responsetranslate'] = response 
        print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    return render(request,'show_prescription.html',context)

@login_required
def update_prescription(request, createprescription_id):
    createprescription = Createprescription.objects.get(pk=createprescription_id)
    form = CreateAppointment(request.POST or None, instance = createprescription)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'update_prescription.html', 
		{'createprescription': createprescription, 'form':form})

@login_required
def delete_prescription (request, createprescription_id):
    createprescription = Createprescription.objects.get(pk= createprescription_id)
    data_context = {'createprescription':createprescription}
    if request.method == 'POST':
        print (request.POST)
        if 'yes' in request.POST:
            createprescription.deleted_date = timezone.now()
            createprescription.save()
            return redirect('profile')
        elif 'no' in request.POST:
            return redirect('profile')
    return render(request,'delete_prescription.html',data_context)


class BlogSearchView(ListView):
    model = Createprescription
    template_name = 'myprescriptions.html'
    context_object_name = 'prescriptions'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Createprescription.objects.filter(patient_username__icontains=query).order_by('date')