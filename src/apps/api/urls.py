
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('auth/', api_doc),
    path('auth/', include('rest_framework.urls')),
]
