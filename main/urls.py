from main.serializers import ProviderSerializer
from django.urls import path

from . import views

urlpatterns = [
    path('provider', views.ProviderClass.as_view(), name='provider'),
    path('service_area', views.ServiceAreaClass.as_view(), name='service_area'),
    path('check', views.CheckServiceArea.as_view(), name='check'),
]
