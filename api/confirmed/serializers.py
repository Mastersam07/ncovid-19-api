from rest_framework import serializers

from .models import Confirmed


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmed
        fields = '__all__'
