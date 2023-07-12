"""
URL configuration for dog_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from dog_app.views import BreadDetail, BreadList
from dog_app.views import DogDetail , DogList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/breads/', BreadList.as_view()),
    path('api/breads/<int:pk>', BreadDetail.as_view()),
    path('api/dogs/', DogList.as_view()),
    path('api/dogs/<int:pk>', DogDetail.as_view()),
]
