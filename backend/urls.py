from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from base import views
from django.contrib import admin



urlpatterns = [
   path("admin/",admin.site.urls),
   path("api/",include('base.urls'))
]
