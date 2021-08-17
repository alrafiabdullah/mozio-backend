from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import Provider
from .serializers import ProviderSerializer


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
