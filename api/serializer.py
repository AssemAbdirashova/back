from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions

from django.contrib.auth.models import User

from api.models import Service, Statistics


class ServiceSerializer(serializers.ModelSerializer):
    # category = CategorySerializer2(read_only=True)
    # category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'
