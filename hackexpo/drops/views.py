"""hackexpo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

def drop_form(request):
    if request.method == "POST":
        print("HERE, ABOUT TO redirect")
        return redirect('/thankyou')
    return render(request, 'drop.html')

def thankyou(request):
    print("HERE, ABOUT TO thank your ass")
    # if request.method == "POST":
    #     print("HERE")
    #     render(request, 'thankyou.html')
    return render(request, 'thankyou.html')

# def execute_drop(request):
#     print("HERE")
#     if request.method == "POST":
#         print("HERE")
#     return render(request, 'drop.html')
