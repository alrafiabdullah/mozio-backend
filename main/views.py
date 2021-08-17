from django.contrib.gis.geos import Point
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


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
        try:
            if int(request.data["id"]) > 0:
                try:
                    provider = Provider.objects.get(id=request.data["id"])
                    serialized_data = ProviderSerializer(provider)
                    return Response(serialized_data.data, status=status.HTTP_200_OK)
                except:
                    return Response({"Provider does not exist!"}, status=status.HTTP_404_NOT_FOUND)

            # to retreive all providers
            providers = Provider.objects.all()
            serialized_data = ProviderSerializer(providers, many=True)

            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        # to create one provider
        try:
            serialized_data = ProviderSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
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

    # caches the get request for 2 hours per request
    @method_decorator(cache_page(60*60*2))
    def get(self, request, *args, **kwargs):
        # to retreive one service area by id
        try:
            if int(request.data["id"]) > 0:
                try:
                    service_area = ServiceArea.objects.get(
                        id=request.data["id"])
                    serialized_data = ServiceAreaSerializer(service_area)
                    return Response(serialized_data.data, status=status.HTTP_200_OK)
                except:
                    return Response({"Service area does not exist!"}, status=status.HTTP_404_NOT_FOUND)

            # to retreive all service areas
            service_areas = ServiceArea.objects.all()
            serialized_data = ServiceAreaSerializer(service_areas, many=True)

            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        # to create one service area
        try:
            serialized_data = ServiceAreaSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
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


class CheckServiceArea(GenericAPIView):
    def get_serializer_class(self):
        return

    def get(self, request, *args, **kwargs):
        # to check if service area exists by longitude and latitude
        try:
            lat = request.data["lat"]
            lng = request.data["lng"]

            # in point (lng, lat), normal is (lat, lng)
            point = Point(float(lng), float(lat))

            service = ServiceArea.objects.filter(location__contains=point)

            if service.exists():
                service_dict = {}
                for serv in service:
                    service_dict.update({
                        serv.id: {
                            "name": serv.name,
                            "price": serv.price,
                            "provider": serv.provider.name,
                        }
                    })

                return Response(service_dict, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
