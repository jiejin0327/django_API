"""django_service URL Configuration

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
from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('recognition/<path:ImgPath>)',views.RecognitionImg),
    path('training/<str:UserId>/<path:ImgPath>',views.Training),
    #/recognition?ImgPath=C:\Imag.jpg
    re_path(r'recognition/*',views.RecognitionImg),
    re_path('training/*',views.Training),
    #re_path('DetectStar/*',views.DetectStar),

]
