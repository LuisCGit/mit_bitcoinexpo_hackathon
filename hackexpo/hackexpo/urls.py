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
from users.views import show_nfts
from django.views.generic import TemplateView
from drops.views import drop_form, execute_drop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drops/', drop_form),
    path('drops/',execute_drop,name="drop_execution")
    #path('user/', show_nfts),
    #path('user/', TemplateView.as_view(template_name="nfts.html"))
]
