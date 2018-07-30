from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Index


app_name = 'pissco_core'
urlpatterns = [

    path('', Index.as_view(), name='index')




]
