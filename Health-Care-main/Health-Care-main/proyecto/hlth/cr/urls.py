"""health URL Configuration

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
from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.registerPage,name = 'register'),
    path('profilepage/',views.profile,name='profile'),
    path('profilepage/<str:username>/',views.profile,name='profile'),
    path('newprescription/', views.create_prescription, name='newprescription'),
    path('myprescriptions/',views.view_prescription_list,name='myprescriptions'),
    path('myprescriptions/show_prescription/<newprescription_id>',views.show_prescription, name= 'show_prescription'),
    path('myprescriptions/update_prescription/<newprescription_id>',views.update_prescription, name= 'update_prescription'),
    path('prescriptionupdate/<int:newprescription_id>',views.update_prescription,name='prescriptionupdate'),    
    path('search-prescriptions/', views.BlogSearchView.as_view(), name='search_prescriptions'),
    path('myprescriptions/deleteprescription/<int:newprescription_id>',views.delete_prescription, name ='deleteprescription'),
    path('searchprescriptions',views.search_prescription, name ='searchprescriptions'),
    path('login/',views.login, name='login' )
]
