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
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from .filters import OrderFilter
from django.views.generic import ListView, DetailView

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

def view_prescription_list(request):
    current_user = request.user    
    prescription = Newprescription.objects.filter(doctor_username = current_user)
    data_result = {'prescription_list': prescription}
    return render (request, 'myprescriptions.html', data_result )


def search_prescription(request):
    if 'q' in request.GET:
        q=request.GET['q']
        prescription=Newprescription.objects.filter(patient_username__icontains=q)
    else:
        prescription= Newprescription.objects.all()
    paginator=Paginator(prescription,2)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render (request, 'myprescriptions.html', {'prescription' : posts_obj} )


def show_prescription(request,newprescription_id):
	newprescription = Newprescription.objects.get(pk=newprescription_id)
	return render(request, 'show_prescription.html', 
		{'newprescription': newprescription})



def update_prescription(request, newprescription_id):
    newprescription = Newprescription.objects.get(pk=newprescription_id)
    form = CreateAppointment(request.POST or None, instance = newprescription)
    if form.is_valid():
        form.save()
        return redirect('myprescriptions')
    return render(request, 'update_prescription.html', 
		{'newprescription': newprescription, 'form':form})


class BlogSearchView(ListView):
    model = Newprescription
    template_name = 'myprescriptions.html'
    context_object_name = 'prescriptions'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Newprescription.objects.filter(patient_username__icontains=query).order_by('date')