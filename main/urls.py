from main.serializers import ProviderSerializer
from django.urls import path

from . import views

urlpatterns = [
    path('provider', views.ProviderClass.as_view(), name='provider'),
]
