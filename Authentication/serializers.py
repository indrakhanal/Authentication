from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
# from django.http import JsonResponse
from requests import Response


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)

    def to_representation(self, instance):
        user = User.objects.all().order_by("-id").values()
        return list(user)


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

   