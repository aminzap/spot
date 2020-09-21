from rest_framework import serializers
from . import models


class SpotSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Spot
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
