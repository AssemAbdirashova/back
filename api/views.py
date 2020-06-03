from django.http import HttpResponse
from requests import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import csv
from api.models import Service, Statistics
from api.serializer import ServiceSerializer


def open(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['id', 'week', 'data'])
    for stat in Statistics.objects.all().values_list('id', 'week', 'data'):
        writer.writerow(stat)

    response['Content-Disposition'] = 'attachment; filename = "stat.csv"'
    return response

class ServiceListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        companies = Service.objects.all()
        serializer = ServiceSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, ):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ServiceDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, service_id):
        try:
            return Service.objects.get(id=service_id)
        except Service.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, service_id):
        service = self.get_object(service_id)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, service_id):
        service = self.get_object(service_id)
        serializer = ServiceSerializer(instance=service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, service_id):
        service = self.get_object(service_id)
        service.delete()

        return Response({'deleted': True})
