"""hlth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from. import views
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('home/',views.home,name='home'),
    path('register/', views.registerPage,name = 'register'),
    path('profilepage/',views.profile,name='profile'),
    path('profilepage/<str:username>',views.profile,name='profile'),
    path('newprescription/', views.create_prescription, name='createprescription'),
    path('myprescriptions',views.view_prescription_list,name='myprescriptions'),
    path('myprescriptionspatients',views.view_prescription_list_patients,name='myprescriptionspatients'),
    path('profilpage/show_prescription/<createprescription_id>',views.translate, name= 'show_prescription'),
    path('profilepage/show_prescription/<createprescription_id>',views.translate, name= 'show_prescription'),
    path('profilepage/update_prescription/<createprescription_id>',views.update_prescription, name= 'update_prescription'),
    path('profilepage/prescriptionupdate/<int:createprescription_id>',views.update_prescription,name='prescriptionupdate'),    
    path('search-prescriptions/', views.BlogSearchView.as_view(), name='search_prescriptions'),
    path('profilepage/deleteprescription/<int:createprescription_id>',views.delete_prescription, name ='deleteprescription'),
    path('searchprescriptions',views.search_prescription, name ='searchprescriptions'),


    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),

]
