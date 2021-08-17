from django.contrib.gis.geos import Point

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


# Create your views here.
class ProviderClass(GenericAPIView):
    serializer_class = ProviderSerializer

    def get(self, request, *args, **kwargs):
        # to retreive one provider by id
        if int(request.data["id"]) > 0:
            try:
                provider = Provider.objects.get(id=request.data["id"])
                serialized_data = ProviderSerializer(provider)
                return Response(serialized_data.data, status=status.HTTP_200_OK)
            except:
                return Response({"Provider does not exist!"}, status=status.HTTP_400_BAD_REQUEST)

        # to retreive all providers
        providers = Provider.objects.all()
        serialized_data = ProviderSerializer(providers, many=True)

        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # to create one provider
        serialized_data = ProviderSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # to delete one provider by id
        try:
            provider = Provider.objects.get(id=request.data['id'])
            provider.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        # to update one provider by id
        try:
            provider = Provider.objects.get(id=request.data['id'])
            serialized_data = ProviderSerializer(provider, data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_200_OK)
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaClass(GenericAPIView):
    serializer_class = ServiceAreaSerializer

    def get(self, request, *args, **kwargs):
        # to retreive one service area by id
        if int(request.data["id"]) > 0:
            try:
                service_area = ServiceArea.objects.get(id=request.data["id"])
                serialized_data = ServiceAreaSerializer(service_area)
                return Response(serialized_data.data, status=status.HTTP_200_OK)
            except:
                return Response({"Service area does not exist!"}, status=status.HTTP_400_BAD_REQUEST)

        # to retreive all service areas
        service_areas = ServiceArea.objects.all()
        serialized_data = ServiceAreaSerializer(service_areas, many=True)

        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # to create one service area
        serialized_data = ServiceAreaSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # to delete one service area by id
        try:
            service_area = ServiceArea.objects.get(id=request.data['id'])
            service_area.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        # to update one service area by id
        try:
            service_area = ServiceArea.objects.get(id=request.data['id'])
            serialized_data = ServiceAreaSerializer(
                service_area, data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_200_OK)
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
