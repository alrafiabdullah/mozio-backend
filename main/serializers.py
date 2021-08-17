from rest_framework.serializers import ModelSerializer

from .models import Provider, ServiceArea


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'
